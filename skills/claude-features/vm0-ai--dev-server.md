# Development Server Launcher

## Description
Start and manage a local development server for common project types (Node, Python, Go, Rust, etc.) within a Claude Code workspace. Use this skill to detect project type, install dependencies if needed, run the dev server process, stream logs, and optionally forward ports.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires filesystem access and process execution to install dependencies and run local servers)

## Instructions
1. Detect the repository or workspace language and framework by inspecting files (package.json, requirements.txt, pyproject.toml, go.mod, Cargo.toml, etc.). Confirm the detected project type with the user.
2. Ask which port to use, whether to install or skip dependency installation, and whether the user wants background execution, log streaming, or port forwarding.
3. For the confirmed project type, run the appropriate setup and start commands: examples include npm install && npm run dev, pip install -r requirements.txt && FLASK_APP=app flask run --host=0.0.0.0, or cargo run --bin <name>. Use virtualenv/venv or node version managers if requested.
4. Stream server logs to the user, watch for successful bind messages or errors, and provide actionable debugging hints if startup fails (missing env vars, port in use, dependency errors).
5. Offer commands or configuration to persist environment variables, set up a reverse proxy, or add the dev server to a devcontainer/launch configuration. Stop and clean up running processes on user request.

## Example Usage
- "Start the dev server for this Node project on port 3000 and stream logs"
- "Detect project type and run the Python Flask app in this workspace"
- "Install dependencies and launch the Go HTTP server, forwarding port 8080"

## Note
This skill runs filesystem commands and processes; ensure you trust and review executed commands. It requires an interactive Claude Code workspace with permissions to run processes and access the project files.
