# Maven Build Lifecycle — Benchflow AI

## Description
Explains the Maven build lifecycle, its standard phases and goals, and how to map goals to concrete mvn commands and plugins. Use this skill when you need a clear, actionable breakdown of what each lifecycle phase does and how to troubleshoot or optimize builds.

## Platforms
- Claude Desktop: Supported
- Claude Code: Supported

## Instructions
1. Ask the user for project context: Maven version, packaging type (jar/war/pom), and which goal or error they are investigating.
2. Present a concise list of Maven lifecycles and the default phases (clean, default: validate, compile, test, package, verify, install, deploy) and what each phase does.
3. For a requested phase or goal, map it to the typical plugins and plugin goals that bind to that phase (for example, compile -> maven-compiler-plugin:compile; test -> surefire:reporting, etc.).
4. Provide precise command examples for common tasks (e.g., mvn clean package, mvn test, mvn install -DskipTests) and explain when to use flags like -DskipTests or -P profiles.
5. Offer troubleshooting steps for common issues: dependency resolution, failing tests, plugin configuration conflicts, and build profiles. Include specific checks (pom.xml, effective-pom, mvn -X) the user should run.
6. If requested, produce a minimal actionable plan to optimize build time or to restructure phases (parallel builds, incremental compilation, plugin versions to upgrade).
7. End with a short summary and point to authoritative references (Maven documentation, plugin docs) for further reading.

## Example Usage
- "Explain the Maven build lifecycle and what happens during 'mvn package'"
- "Which plugins run during the install phase and how can I speed up my Maven build?"
- "I get dependency errors during mvn test — what should I check first?"

## Note
I cannot run mvn commands or inspect your filesystem; provide relevant pom.xml snippets or error logs for more specific guidance.