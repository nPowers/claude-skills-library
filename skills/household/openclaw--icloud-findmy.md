# iCloud Find My Helper

## Description
Guides users through using Apple's iCloud Find My to locate devices, share location, enable Lost Mode, and secure or erase lost items. Use when you need clear, step-by-step instructions, troubleshooting, or example messages for contact and recovery.

## Platforms
- Claude Desktop: Supported
- Claude Code: Not Supported (conversational guidance only; no code execution or system/API access)

## Instructions
1. Ask the user what they want to do (locate a device, share location, enable Lost Mode, erase a device, or secure an account) and which device or Apple ID is involved.
2. Confirm whether the user can access an Apple device (iPhone/iPad/Mac) or iCloud.com and whether they know the Apple ID credentials and have two-factor authentication available.
3. If locating a device, present platform-specific, step-by-step instructions:
   - On iPhone/iPad: open Settings → tap name → Find My → Find My iPhone; or open the Find My app → Devices → select device → choose Play Sound, Directions, or Mark as Lost.
   - On Mac: open System Settings → click Apple ID → iCloud → Find My; or open the Find My app → Devices → select device → take an action.
   - On the web: sign in to iCloud.com → Find iPhone → select device → Play Sound, Lost Mode, or Erase.
4. Explain Lost Mode in detail: what it does, how to enable it, and what information to display (contact phone, brief recovery message). Provide a short, editable message template.
5. Describe the Erase Device option and its consequences (permanent local data erase, activation lock remains). Warn that erase is irreversible and should be used only when recovery is impossible or the device is compromised.
6. Walk through location sharing and Family Sharing: how to enable Share My Location, add family members, and check location permissions in Messages and Contacts.
7. Provide security steps if account compromise is suspected: change Apple ID password, sign out suspicious devices, review trusted phone numbers and devices, enable/review two-factor authentication settings.
8. Offer troubleshooting tips for common problems: device offline, low battery, Location Services turned off, iCloud not signed in, outdated OS, and how to check device status in Find My.
9. When asked, produce concise outputs: a prioritized to-do checklist, step-by-step guide tailored to the user's platform, or ready-to-send messages and templates for Lost Mode or contacting authorities.
10. Always include a brief reminder that the assistant cannot access iCloud or perform actions on behalf of the user—only provide instructions and templates.

## Example Usage
- "Help me find my iPhone that's offline — what should I do?"
- "How do I put a lost iPad into Lost Mode and leave a contact message?"
- "Walk me through using iCloud.com to locate my son's MacBook and secure the account."

## Note
The user must have their Apple ID credentials and access to two-factor authentication to perform actions. The assistant only provides guidance and cannot interact with Apple services or access accounts. For safety or theft, consider contacting local authorities in addition to using Find My. For the original skill reference, see: https://smithery.ai/skills/openclaw/icloud-findmy