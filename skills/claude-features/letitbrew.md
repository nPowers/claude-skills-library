# LetItBrew — macOS Keep-Awake Menu App

## Description
A lightweight, open-source macOS menu-bar utility that uses lifecycle hooks to keep a Mac awake for long-running Claude Code, Codex, OpenCode, or GitHub Copilot CLI sessions. Use it when you need to prevent sleep while background agents or CLI-based assistants are working.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local macOS integration and lifecycle hook installation)

## Instructions
1. Confirm you are on a supported macOS version and have local development privileges.
2. Clone the repository and follow the project's build/install steps (e.g., git clone <repo>, build or install the .app into /Applications) according to the repo README.
3. Install or enable LetItBrew so the app appears in the macOS menu bar.
4. Configure your Claude Code / Copilot CLI lifecycle hooks to call LetItBrew controls: start keep-awake at job start and stop keep-awake at job finish.
5. When running long-running model tasks, ensure LetItBrew shows an active state in the menu bar and verify system sleep is inhibited.
6. After tasks complete, verify the lifecycle hook stops the keep-awake mode so normal sleep behavior resumes.

## Example Usage
- "Keep my Mac awake while Claude Code runs a long training job using LetItBrew"
- "Install LetItBrew and add lifecycle hooks to start/stop keep-awake around my Codex sessions"
- "Verify LetItBrew is active during a Copilot CLI background task"

## Note
macOS-only utility; requires local installation and permission to prevent system sleep. Follow the project README for specific build and security prompts.