# Clawd Conduit

## Description
Clawd Conduit connects Claude Code to the Clawd on Desk device, implementing full-lifecycle hook wiring so desktop permission prompts and device events can be handled from the development environment. It supports all lifecycle events for integrated automation.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires local device access and permission handling)

## Instructions
1. Install the Clawd Conduit plugin into your Claude Code environment and confirm communication with the Clawd on Desk device.
2. Authorize required device permissions on the host OS when prompted so the conduit can observe and respond to device events.
3. Map the 15 lifecycle hook events you need to the corresponding handler behaviors (e.g., notify user, approve action, log telemetry locally).
4. Describe the desktop prompt flows and expected automatic responses; configure safe defaults and escalation rules for ambiguous prompts.
5. Trigger events through the device or simulated inputs; monitor logs and iterate on handler logic until behaviors are reliable.
6. For production use, lock down permission scopes and audit automatic responses to avoid unintended actions.

## Example Usage
- "Install Clawd Conduit and register lifecycle handlers for device connect and permission requests"
- "Configure the conduit to auto-respond to media playback prompts but require prompt for firmware updates"
- "Show me the recent device lifecycle events and the conduit responses"

## Note
Requires local device access and OS-level permissions. Use caution when enabling automatic responses to sensitive prompts; review and test handlers in a safe environment.