# Salavender Git Workflow

## Description
A Claude Code skill that provides a git-centric workflow assistant: it generates commit messages, suggests branch names, formats PR descriptions using templates, and automates common branching and merge tasks. Use this to standardize commits, speed PR creation, and apply project-specific git conventions.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local git and filesystem access to read repository state and run git commands)

## Instructions
1. Open the target repository in your Claude Code workspace (ensure git is initialized and your changes are present).
2. Ask the skill to analyze the working tree or staged changes to produce a concise commit message or changelog entry.
3. Request a branch naming suggestion or create a feature branch using the recommended convention.
4. Use the skill to generate a PR title and body from a template, including checklist items and relevant issue links.
5. Optionally run pre-push or validation hooks suggested by the skill (linters, tests) before pushing.
6. Push the branch and open a pull request using the generated description; update template fields as needed.
7. Customize commit and PR templates stored in the repository to match your team’s workflow and rerun the skill.

## Example Usage
- "Create a commit message for my staged changes"
- "Suggest a branch name for this feature: user authentication"
- "Generate a PR description using the team's template for this branch"

## Note
This skill needs git installed and access to the repository files; it will not run on Claude Desktop. Always review generated commits and PR text before pushing to remote branches.