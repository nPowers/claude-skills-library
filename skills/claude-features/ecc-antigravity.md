# ECC-Antigravity Runtime

## Description
A Claude Code skill to install, launch, and manage the ECC (Everything Claude Code) runtime for the Google Antigravity project. Use it to deploy the multi-agent runtime (68+ specialized agents, 280+ skills) and enable the automated safety and quality lifecycle hooks powered by Gemini 3.8.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires repository cloning, dependency installation, and runtime process orchestration)

## Instructions
1. Confirm prerequisites: ensure you have a Claude Code execution environment with git, Docker (or container runtime), and a suitable Python/Node toolchain installed. Have your Gemini 3.8 API key or credentials ready if you plan to use the Gemini-powered hooks.
2. Clone the repository: git clone https://github.com/cloudblower/ECC-Antigravity
3. Inspect repository docs: cd ECC-Antigravity and read the README and any CONTRIBUTING or INSTALL files to confirm exact commands and supported runtime images.
4. Install dependencies: follow the repo instructions. Typical actions are:
   - pip install -r requirements.txt (for Python components)
   - npm install (for Node components)
   - or run the provided setup script: ./setup.sh
5. Configure the runtime: copy example environment/config files (for example, cp .env.example .env) and set GEMINI_API_KEY, ports, agent selection, and lifecycle hook options according to your needs.
6. Start the runtime: use the repository's recommended launch method, e.g. docker-compose up -d or the provided start command (python -m ecc_antigravity.server run or an equivalent script). Use the repo docs for the exact command.
7. Verify deployment: check health endpoints, list available agents/skills, and run a supplied sample skill to confirm functionality. Monitor logs (docker logs or the process stdout) to observe the safety/quality hook activity.
8. Operate and extend: enable or tune automated lifecycle hooks in the configuration to control safety checks, quality gates, and telemetry. Deploy or disable individual agents/skills as your workload requires.
9. Stop and clean up: shut down services gracefully (docker-compose down or the recommended stop command) and rotate/secure any API keys or credentials after use.

## Example Usage
- "Start the ECC-Antigravity runtime and enable Gemini hooks"
- "Deploy Antigravity agents and run a sample skill"
- "Run health checks for ECC-Antigravity and list active agents"

## Note
This project is intended for use inside a Code execution environment; follow the repository's README for exact commands and versions. You will typically need access to Gemini 3.8 credentials and to accept any community-maintained project limitations or license terms.