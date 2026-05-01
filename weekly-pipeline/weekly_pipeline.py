#!/usr/bin/env python3.11
"""
weekly_pipeline.py — Claude Skills Weekly Discovery & Rewrite Pipeline
=======================================================================
Optimized for low credit usage. Runs weekly to discover, deduplicate,
rewrite, and package new Claude skills across 4 tracks:
  1. Professional / Domain-Specific
  2. Software Development by Language
  3. Everyday Household / Busy Family
  4. New Claude Features & Hooks

Outputs:
  - Rewritten SKILL.md files in /output/YYYY-WW/
  - Summary spreadsheet (Excel)
  - Email delivery to configured recipient
  - SQLite tracking DB to prevent duplicates

Usage:
  python3.11 weekly_pipeline.py [--dry-run] [--track TRACK_NAME]
"""

import os
import sys
import json
import sqlite3
import argparse
import datetime
import time
import zipfile
import smtplib
import requests
import openpyxl
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from openai import OpenAI

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

BASE_DIR = Path("/home/ubuntu/claude-skills-research")
OUTPUT_DIR = BASE_DIR / "output"
DB_PATH = BASE_DIR / "seen_skills.db"
TRACK_DEFS_PATH = BASE_DIR / "track_definitions.py"

EMAIL_TO = "anadventuringnerd@gmail.com"
EMAIL_FROM = os.environ.get("EMAIL_FROM", "")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GITHUB_HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if GITHUB_TOKEN:
    GITHUB_HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"

# Items per track per week
ITEMS_PER_TRACK = 20

# LLM model — use the cheapest capable model
LLM_MODEL = "gpt-4.1-mini"

# Batch size for LLM rewrites (5 skills per API call = major credit savings)
REWRITE_BATCH_SIZE = 5

# ─────────────────────────────────────────────────────────────────────────────
# DATABASE SETUP
# ─────────────────────────────────────────────────────────────────────────────

def init_db():
    """Initialize SQLite tracking database."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS seen_skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skill_key TEXT UNIQUE NOT NULL,
            track TEXT NOT NULL,
            name TEXT NOT NULL,
            source_url TEXT,
            processed_date TEXT NOT NULL,
            week_label TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def is_seen(conn, skill_key: str) -> bool:
    c = conn.cursor()
    c.execute("SELECT 1 FROM seen_skills WHERE skill_key = ?", (skill_key,))
    return c.fetchone() is not None


def mark_seen(conn, skill_key: str, track: str, name: str, source_url: str, week_label: str):
    c = conn.cursor()
    try:
        c.execute("""
            INSERT INTO seen_skills (skill_key, track, name, source_url, processed_date, week_label)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (skill_key, track, name, source_url, datetime.date.today().isoformat(), week_label))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # Already seen, skip silently


# ─────────────────────────────────────────────────────────────────────────────
# GITHUB DISCOVERY
# ─────────────────────────────────────────────────────────────────────────────

def search_github(query: str, min_stars: int = 5, days_back: int = 90) -> list[dict]:
    """
    Search GitHub for repositories matching the query.
    Filters by minimum stars and recency to keep quality high.
    Returns a list of {name, full_name, description, url, stars, updated_at}.
    """
    since_date = (datetime.date.today() - datetime.timedelta(days=days_back)).isoformat()
    search_query = f"{query} pushed:>{since_date} stars:>={min_stars}"
    url = "https://api.github.com/search/repositories"
    params = {
        "q": search_query,
        "sort": "updated",
        "order": "desc",
        "per_page": 30,
    }
    try:
        resp = requests.get(url, headers=GITHUB_HEADERS, params=params, timeout=15)
        if resp.status_code == 200:
            items = resp.json().get("items", [])
            return [
                {
                    "name": item["name"],
                    "full_name": item["full_name"],
                    "description": item.get("description") or "",
                    "url": item["html_url"],
                    "stars": item["stargazers_count"],
                    "updated_at": item["updated_at"][:10],
                    "topics": item.get("topics", []),
                }
                for item in items
            ]
    except Exception as e:
        print(f"  [WARN] GitHub search failed for '{query}': {e}")
    return []


def fetch_readme(full_name: str) -> str:
    """Fetch the README for a GitHub repo (first 3000 chars to save tokens)."""
    url = f"https://api.github.com/repos/{full_name}/readme"
    try:
        resp = requests.get(url, headers=GITHUB_HEADERS, timeout=10)
        if resp.status_code == 200:
            import base64
            content = resp.json().get("content", "")
            decoded = base64.b64decode(content).decode("utf-8", errors="ignore")
            return decoded[:3000]
    except Exception:
        pass
    return ""


def search_smithery(query: str, max_results: int = 20) -> list[dict]:
    """
    Scrape Smithery skills search results.
    Returns a list of {name, description, installs, url}.
    """
    url = f"https://smithery.ai/skills?q={requests.utils.quote(query)}"
    try:
        resp = requests.get(url, timeout=15, headers={
            "User-Agent": "Mozilla/5.0 (compatible; ClaudeSkillsBot/1.0)"
        })
        if resp.status_code == 200:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(resp.text, "html.parser")
            results = []
            # Smithery skill cards typically have an <a> with the skill path
            for link in soup.find_all("a", href=True):
                href = link["href"]
                if href.startswith("/skills/") and href.count("/") == 2:
                    skill_path = href[8:]  # Remove /skills/
                    text = link.get_text(separator=" ", strip=True)[:500]
                    results.append({
                        "name": skill_path.replace("/", "--"),
                        "full_name": skill_path,
                        "description": text,
                        "url": f"https://smithery.ai{href}",
                        "stars": 0,
                        "updated_at": datetime.date.today().isoformat(),
                        "source": "smithery",
                    })
                    if len(results) >= max_results:
                        break
            return results
    except Exception as e:
        print(f"  [WARN] Smithery search failed for '{query}': {e}")
    return []


# ─────────────────────────────────────────────────────────────────────────────
# LLM BATCH REWRITER
# ─────────────────────────────────────────────────────────────────────────────

REWRITE_SYSTEM_PROMPT = """You are an expert at writing Claude AI skills in the proper Manus SKILL.md format.

A proper Claude skill has this exact structure:

# [Skill Display Name]

## Description
[1-3 sentences: what the skill does, when to use it, key capabilities]

## Platforms
- Claude Desktop: Supported / Not Supported
- Claude Code: Supported / Not Supported (with brief reason if Code-only)

## Instructions
[Numbered steps Claude should follow when this skill is activated. Be specific and actionable.]

## Example Usage
- "[Trigger phrase 1]"
- "[Trigger phrase 2]"
- "[Trigger phrase 3]"

## Note
[Any important caveats, limitations, or disclaimers. Keep brief.]

RULES:
- Skills that require file system access, code execution, or Bash are Claude Code only.
- Skills that only need knowledge and conversation work in both platforms.
- MCP-based skills work in Claude Desktop if the MCP server is installed.
- Sub-agent orchestrators are Claude Code only.
- Do NOT copy source text verbatim — rewrite in original language.
- Keep descriptions concise but information-rich.
- Output valid Markdown only, no extra commentary.
"""

def batch_rewrite_skills(raw_skills: list[dict], track_label: str) -> list[dict]:
    """
    Rewrite a batch of raw skill descriptions into proper SKILL.md format.
    Uses a single LLM call per batch of REWRITE_BATCH_SIZE to minimize credits.
    Returns list of {name, display_name, category, markdown, platform_desktop, platform_code}.
    """
    client = OpenAI()
    results = []

    for i in range(0, len(raw_skills), REWRITE_BATCH_SIZE):
        batch = raw_skills[i:i + REWRITE_BATCH_SIZE]
        batch_input = json.dumps([
            {
                "index": j,
                "name": s.get("name", ""),
                "description": s.get("description", ""),
                "source_url": s.get("url", ""),
                "track": track_label,
                "stars": s.get("stars", 0),
            }
            for j, s in enumerate(batch)
        ], indent=2)

        user_prompt = f"""Rewrite the following {len(batch)} Claude skills into proper SKILL.md format.
Return a JSON array with one object per skill containing:
- "index": the original index number
- "display_name": a clear, professional display name
- "category": the most appropriate category for this skill
- "platform_desktop": true or false
- "platform_code": true or false
- "markdown": the complete SKILL.md content as a string

Input skills:
{batch_input}

Return ONLY a valid JSON array, no other text."""

        try:
            response = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {"role": "system", "content": REWRITE_SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.3,
                max_tokens=4000,
            )
            content = response.choices[0].message.content.strip()
            # Strip markdown code fences if present
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
            parsed = json.loads(content)
            for item in parsed:
                idx = item.get("index", 0)
                if idx < len(batch):
                    original = batch[idx]
                    results.append({
                        "name": original.get("name", f"skill-{i+idx}"),
                        "display_name": item.get("display_name", original.get("name", "")),
                        "category": item.get("category", "General"),
                        "platform_desktop": item.get("platform_desktop", True),
                        "platform_code": item.get("platform_code", True),
                        "markdown": item.get("markdown", ""),
                        "source_url": original.get("url", ""),
                        "stars": original.get("stars", 0),
                        "updated_at": original.get("updated_at", ""),
                    })
        except Exception as e:
            print(f"  [ERROR] LLM rewrite failed for batch {i}: {e}")
            # Fallback: use raw description
            for j, s in enumerate(batch):
                results.append({
                    "name": s.get("name", f"skill-{i+j}"),
                    "display_name": s.get("name", "").replace("-", " ").title(),
                    "category": "General",
                    "platform_desktop": True,
                    "platform_code": True,
                    "markdown": f"# {s.get('name', 'Skill')}\n\n## Description\n{s.get('description', '')}\n",
                    "source_url": s.get("url", ""),
                    "stars": s.get("stars", 0),
                    "updated_at": s.get("updated_at", ""),
                })
        time.sleep(1)  # Rate limiting

    return results


# ─────────────────────────────────────────────────────────────────────────────
# SKILL FILE WRITER
# ─────────────────────────────────────────────────────────────────────────────

def save_skill_file(skill: dict, output_dir: Path) -> Path:
    """Save a rewritten skill to a .md file."""
    safe_name = skill["name"].replace("/", "-").replace(" ", "-").lower()
    filepath = output_dir / f"{safe_name}.md"
    filepath.write_text(skill["markdown"], encoding="utf-8")
    return filepath


# ─────────────────────────────────────────────────────────────────────────────
# SPREADSHEET BUILDER
# ─────────────────────────────────────────────────────────────────────────────

def build_weekly_spreadsheet(all_skills: list[dict], week_label: str, output_dir: Path) -> Path:
    """Build a summary Excel spreadsheet for the week's skills."""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = f"Week {week_label}"

    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    HEADER_FILL = PatternFill("solid", fgColor="1F3864")
    YES_FILL = PatternFill("solid", fgColor="C6EFCE")
    NO_FILL = PatternFill("solid", fgColor="FFCCCC")
    HEADER_FONT = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
    BODY_FONT = Font(name="Calibri", size=10)
    WRAP = Alignment(wrap_text=True, vertical="top")
    CENTER = Alignment(horizontal="center", vertical="top")
    THIN = Side(style="thin", color="CCCCCC")
    BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

    headers = ["Track", "Category", "Name", "Display Name", "Claude Desktop",
               "Claude Code", "Stars", "Source URL", "File"]
    col_widths = [25, 25, 30, 35, 16, 14, 8, 50, 35]

    for col_idx, (h, w) in enumerate(zip(headers, col_widths), 1):
        cell = ws.cell(row=1, column=col_idx, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = CENTER
        cell.border = BORDER
        ws.column_dimensions[get_column_letter(col_idx)].width = w

    ws.freeze_panes = "A2"

    for row_idx, skill in enumerate(all_skills, 2):
        row_data = [
            skill.get("track_label", ""),
            skill.get("category", ""),
            skill.get("name", ""),
            skill.get("display_name", ""),
            "✓" if skill.get("platform_desktop") else "✗",
            "✓" if skill.get("platform_code") else "✗",
            skill.get("stars", "N/A"),
            skill.get("source_url", ""),
            skill.get("file_path", ""),
        ]
        for col_idx, val in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.font = BODY_FONT
            cell.border = BORDER
            cell.alignment = WRAP
            if col_idx == 5:
                cell.fill = YES_FILL if skill.get("platform_desktop") else NO_FILL
                cell.alignment = CENTER
            elif col_idx == 6:
                cell.fill = YES_FILL if skill.get("platform_code") else NO_FILL
                cell.alignment = CENTER
        ws.row_dimensions[row_idx].height = 40

    xlsx_path = output_dir / f"Claude_Skills_Week_{week_label}.xlsx"
    wb.save(xlsx_path)
    return xlsx_path


# ─────────────────────────────────────────────────────────────────────────────
# EMAIL DELIVERY
# ─────────────────────────────────────────────────────────────────────────────

def send_email(zip_path: Path, xlsx_path: Path, week_label: str, summary: dict):
    """Send the weekly package via email."""
    if not EMAIL_FROM or not EMAIL_PASSWORD:
        print("[WARN] Email credentials not configured. Skipping email delivery.")
        print(f"  Set EMAIL_FROM and EMAIL_PASSWORD environment variables.")
        print(f"  Output saved to: {zip_path}")
        return False

    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = f"🤖 Claude Skills Weekly Update — Week {week_label}"

    body = f"""
Hi,

Your weekly Claude Skills & Agents update is ready for review.

📊 Week {week_label} Summary:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for track_label, count in summary.items():
        body += f"  • {track_label}: {count} new skills\n"

    body += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total new skills this week: {sum(summary.values())}

Attached:
  📦 ZIP file with all rewritten SKILL.md files
  📊 Excel spreadsheet with full details and compatibility flags

Please review and test before publishing to the AI Compare repo.

— Manus AI Weekly Pipeline
"""
    msg.attach(MIMEText(body, "plain"))

    for attachment_path in [zip_path, xlsx_path]:
        if attachment_path.exists():
            with open(attachment_path, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={attachment_path.name}")
            msg.attach(part)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print(f"✅ Email sent to {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"[ERROR] Email delivery failed: {e}")
        return False


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE
# ─────────────────────────────────────────────────────────────────────────────

def run_pipeline(dry_run: bool = False, track_filter: str = None):
    """Main weekly pipeline execution."""
    # Import track definitions
    import importlib.util
    spec = importlib.util.spec_from_file_location("track_definitions", TRACK_DEFS_PATH)
    track_defs_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(track_defs_module)
    TRACKS = track_defs_module.TRACKS

    week_label = datetime.date.today().strftime("%Y-W%V")
    week_dir = OUTPUT_DIR / week_label
    week_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"  Claude Skills Weekly Pipeline — {week_label}")
    print(f"  Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"{'='*60}\n")

    conn = init_db()
    all_skills_this_week = []
    summary = {}

    for track_key, track in TRACKS.items():
        if track_filter and track_key != track_filter:
            continue

        track_label = track["label"]
        print(f"\n📂 Track: {track['emoji']} {track_label}")
        print(f"   Searching GitHub and Smithery...")

        # ── Discover ──────────────────────────────────────────────────────────
        raw_candidates = []

        # First: use seed skills (always fresh on first run)
        for seed in track.get("seed_skills", []):
            skill_key = f"seed::{seed['name']}"
            if not is_seen(conn, skill_key):
                seed["url"] = seed.get("url", f"seed://{seed['name']}")
                seed["source"] = "seed"
                raw_candidates.append(seed)

        # Then: search GitHub
        for query in track.get("github_queries", [])[:3]:  # Limit to 3 queries/track
            results = search_github(query, min_stars=3, days_back=60)
            for r in results:
                skill_key = f"github::{r['full_name']}"
                if not is_seen(conn, skill_key) and r not in raw_candidates:
                    r["source"] = "github"
                    raw_candidates.append(r)
            time.sleep(0.5)  # Respect rate limits

        # Then: search Smithery
        for query in track.get("smithery_queries", [])[:2]:  # Limit to 2 queries/track
            results = search_smithery(query, max_results=15)
            for r in results:
                skill_key = f"smithery::{r['full_name']}"
                if not is_seen(conn, skill_key) and r not in raw_candidates:
                    r["source"] = "smithery"
                    raw_candidates.append(r)
            time.sleep(0.5)

        # ── Deduplicate & Limit ───────────────────────────────────────────────
        # Sort by stars descending, then take top ITEMS_PER_TRACK
        raw_candidates.sort(key=lambda x: x.get("stars", 0), reverse=True)
        selected = raw_candidates[:ITEMS_PER_TRACK]

        print(f"   Found {len(raw_candidates)} candidates → selected {len(selected)} new items")

        if not selected:
            print(f"   [SKIP] No new items for this track this week.")
            summary[track_label] = 0
            continue

        if dry_run:
            print(f"   [DRY RUN] Would rewrite {len(selected)} skills")
            for s in selected[:3]:
                print(f"     - {s.get('name', 'N/A')}: {s.get('description', '')[:80]}...")
            summary[track_label] = len(selected)
            continue

        # ── Rewrite ───────────────────────────────────────────────────────────
        print(f"   Rewriting {len(selected)} skills via LLM (batches of {REWRITE_BATCH_SIZE})...")
        rewritten = batch_rewrite_skills(selected, track_label)

        # ── Save Files ────────────────────────────────────────────────────────
        track_dir = week_dir / track_key
        track_dir.mkdir(exist_ok=True)

        for skill in rewritten:
            skill["track_label"] = track_label
            file_path = save_skill_file(skill, track_dir)
            skill["file_path"] = str(file_path.name)
            all_skills_this_week.append(skill)

            # Mark as seen in DB
            source_type = "github" if "github.com" in skill.get("source_url", "") else "smithery"
            skill_key = f"{source_type}::{skill['name']}"
            mark_seen(conn, skill_key, track_key, skill["name"],
                      skill.get("source_url", ""), week_label)

        summary[track_label] = len(rewritten)
        print(f"   ✅ Saved {len(rewritten)} skills to {track_dir}")

    if dry_run:
        print(f"\n[DRY RUN] Pipeline complete. No files written.")
        conn.close()
        return

    if not all_skills_this_week:
        print("\n[INFO] No new skills discovered this week. Nothing to deliver.")
        conn.close()
        return

    # ── Build Spreadsheet ─────────────────────────────────────────────────────
    print(f"\n📊 Building weekly spreadsheet...")
    xlsx_path = build_weekly_spreadsheet(all_skills_this_week, week_label, week_dir)
    print(f"   Saved: {xlsx_path}")

    # ── Create ZIP ────────────────────────────────────────────────────────────
    zip_path = OUTPUT_DIR / f"Claude_Skills_{week_label}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for skill in all_skills_this_week:
            track_key_for_skill = skill["track_label"].lower().replace(" ", "_").replace("/", "_")
            file_path = week_dir / track_key_for_skill.replace(" ", "_") / skill["file_path"]
            if not file_path.exists():
                # Try finding the file in any subdirectory
                for sub in week_dir.iterdir():
                    candidate = sub / skill["file_path"]
                    if candidate.exists():
                        file_path = candidate
                        break
            if file_path.exists():
                zf.write(file_path, f"{week_label}/{skill['track_label']}/{skill['file_path']}")
        zf.write(xlsx_path, f"{week_label}/Claude_Skills_Week_{week_label}.xlsx")
    print(f"   ZIP: {zip_path}")

    # ── Email Delivery ────────────────────────────────────────────────────────
    print(f"\n📧 Sending email to {EMAIL_TO}...")
    send_email(zip_path, xlsx_path, week_label, summary)

    # ── Final Summary ─────────────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  ✅ Weekly Pipeline Complete — {week_label}")
    print(f"{'='*60}")
    total = sum(summary.values())
    for track_label, count in summary.items():
        print(f"  {count:3d} skills — {track_label}")
    print(f"  ───────────────────────────────")
    print(f"  {total:3d} total new skills this week")
    print(f"\n  Output: {week_dir}")
    print(f"  ZIP:    {zip_path}")
    print(f"  DB:     {DB_PATH}")

    conn.close()


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Claude Skills Weekly Pipeline")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run without writing files or sending email")
    parser.add_argument("--track", type=str, default=None,
                        help="Run only a specific track (professional/development/household/claude_features)")
    args = parser.parse_args()
    run_pipeline(dry_run=args.dry_run, track_filter=args.track)
