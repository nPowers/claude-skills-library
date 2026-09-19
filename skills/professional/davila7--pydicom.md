# DICOM Processing with pydicom

## Description
A code-oriented skill for working with medical DICOM files using the pydicom Python library: parsing metadata, anonymizing, extracting pixel data, and producing summaries or conversion-ready outputs. Use when you need reproducible file operations or programmatic image handling.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires Python runtime and file-system access to read/write DICOM files)

## Instructions
1. Ask the user to describe the goal (e.g., anonymize, extract series, convert to PNG, summarize metadata) and provide path(s) to the DICOM file(s) or indicate how files will be made available to the runtime.
2. Validate the environment: confirm pydicom is installed and accessible, and request the target output directory and any naming conventions.
3. When appropriate, generate a clear, minimal Python script or code cell using pydicom that performs the requested task (read file, inspect/modify tags, save, extract pixels, anonymize with a chosen profile).
4. Include safe defaults for PHI removal (list of tags to remove or replace) and warn about irreversibility of destructive operations; offer a dry-run mode that prints changes without writing files.
5. If pixel data is extracted, provide recommended libraries and code for downstream steps (numpy, Pillow, SimpleITK) and include example commands to visualize or convert images.
6. Provide verification steps the user can run to confirm integrity (count of files, checksum, sample tag output) and sample unit-test snippets where appropriate.
7. End with suggested next steps and a brief troubleshooting checklist for common pydicom errors.

## Example Usage
- "Anonymize all DICOMs in /data/study1 and save to /data/anonymized — show the pydicom script."
- "Extract slices from this DICOM series and save as PNG files with windowing applied."
- "Show a python snippet that reads a DICOM, prints PatientID and StudyDate, and replaces PatientName."

## Note
This skill executes or produces code that requires access to the file system and a Python environment. Handle protected health information (PHI) in accordance with applicable law and institutional policy; verify anonymization results before sharing data.