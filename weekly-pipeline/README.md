# Weekly Pipeline — Setup & Configuration

The pipeline automatically discovers, rewrites, and packages new Claude skills every week.

## Requirements

```bash
pip install openai openpyxl requests beautifulsoup4
```

## Configuration

Set these environment variables before running:

| Variable | Required | Description |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Used for LLM skill rewrites |
| `GITHUB_TOKEN` | Recommended | Increases GitHub API rate limits from 60 to 5000 req/hr |
| `EMAIL_FROM` | Optional | Gmail address to send weekly report from |
| `EMAIL_PASSWORD` | Optional | Gmail App Password (not your main password) |
| `SMTP_HOST` | Optional | Defaults to `smtp.gmail.com` |
| `SMTP_PORT` | Optional | Defaults to `587` |

## Running the Pipeline

```bash
# Full live run (all 4 tracks)
python3 weekly_pipeline.py

# Dry run — shows what would be processed without writing files
python3 weekly_pipeline.py --dry-run

# Run a single track only
python3 weekly_pipeline.py --track household
python3 weekly_pipeline.py --track professional
python3 weekly_pipeline.py --track development
python3 weekly_pipeline.py --track claude_features
```

## Output Structure

Each run creates a dated folder under `output/`:

```
output/
├── 2026-W18/
│   ├── professional/
│   │   └── *.md
│   ├── development/
│   │   └── *.md
│   ├── household/
│   │   └── *.md
│   ├── claude_features/
│   │   └── *.md
│   └── Claude_Skills_Week_2026-W18.xlsx
└── Claude_Skills_2026-W18.zip
```

## Deduplication

The pipeline maintains `seen_skills.db` (SQLite) to track all previously processed skills. This file is gitignored and stays local. If you delete it, the pipeline will reprocess all seeds on the next run.

## Adding Email Delivery

1. Create a Gmail App Password at https://myaccount.google.com/apppasswords
2. Set `EMAIL_FROM=youraddress@gmail.com` and `EMAIL_PASSWORD=your-app-password`
3. The pipeline will automatically email the ZIP and spreadsheet after each run

## Customizing Tracks

Edit `track_definitions.py` to:
- Add new GitHub search queries to a track
- Add new Smithery search terms
- Add seed skills that should always be included on first run
- Add new tracks entirely
