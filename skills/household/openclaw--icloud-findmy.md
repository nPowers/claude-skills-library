# iCloud Find My Helper

## Description
A code-first assistant that orchestrates authenticated interactions with Apple iCloud "Find My" functionality: locating devices, playing sounds, marking devices lost, and returning device status. Use this when you need programmatic access to Find My features from a trusted, developer-managed environment.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires network calls and Apple authentication)

## Instructions
1. Require explicit user instruction to supply valid authentication credentials/tokens (Apple ID, app-specific password, or OAuth token) and clearly warn about sensitive data handling.
2. Validate authentication by attempting a non-destructive status request for the account; report authentication success or the specific error returned.
3. Provide functions for common operations: a) list devices with metadata (name, model, last seen, battery, location timestamp), b) request current location, c) play a sound on a device, d) mark a device as lost (send message/lock), and e) remotely erase (if supported and confirmed).
4. For each operation, perform API calls with appropriate error handling and return a concise result object that includes success/failure, timestamps, returned coordinates (with human-readable address if reverse geocoding is available), and any relevant warnings (e.g., low battery, device offline).
5. If a location is returned, summarize steps the user should take (e.g., contact local police before remote erase, verify the address, notify family members).
6. Log actions and responses for auditing and require re-confirmation for destructive operations (erase, remove from account, mark as lost).
7. Always respect user privacy and local law; prompt for explicit confirmation before taking any action that changes device state.

## Example Usage
- "Authenticate with my app password and list all devices on my Apple account"
- "Locate my iPhone and give me the last known address"
- "Play a sound on the lost iPad, then mark it as lost if I confirm"

## Note
This skill performs networked, authenticated operations and must be deployed with secure handling of credentials and compliance with Apple terms of service and local privacy laws. Destructive actions require explicit user confirmation and cannot be undone.