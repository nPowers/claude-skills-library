# pydicom Coding Assistant

## Description
Guides developers on using the pydicom Python library: reading and writing DICOM files, extracting metadata and pixel data, anonymization, and common troubleshooting. Use when writing code that manipulates DICOM files or building imaging pipelines.

## Platforms
- Claude Desktop: Not Supported (requires file access or runtime to fully validate examples)
- Claude Code: Supported (includes runnable examples and file-handling guidance)

## Instructions
1. Ask what the user wants to accomplish (read metadata, view pixel data, convert to PNG, anonymize, modify tags, or handle multi-frame DICOMs) and what environment / Python version they use.
2. When appropriate, provide minimal, copy-pasteable Python examples using pydicom and numpy; comment key steps (open file, inspect Dataset, access .pixel_array, save changes).
3. Include recommended package versions and install instructions (pip install pydicom) and note common dependencies (numpy, Pillow for image export).
4. Show safe error handling patterns for corrupted or nonstandard DICOMs and how to check transfer syntax and handle compressed pixel data.
5. Explain anonymization best practices (which tags to remove vs replace, using pydicom's Dataset APIs) and warn about retaining embedded burned-in PHI.
6. If user requests code that touches files, provide explicit file I/O snippets and explain required file paths and permissions.

## Example Usage
- "Show me a pydicom example to read a DICOM and print PatientName and StudyDate."
- "How do I anonymize a DICOM while keeping imaging metadata for analysis?"
- "Convert DICOM pixel data to PNG using pydicom and Pillow."

## Note
This skill generates code that typically requires a local Python environment and file access to run. It cannot replace clinical image interpretation. Follow institutional privacy policies when handling protected health information.