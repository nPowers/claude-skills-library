# DICOM Processing with pydicom

## Description
Provide practical code patterns and guidance for reading, inspecting, anonymizing, and converting DICOM files using the pydicom Python library. Use when developing image-processing pipelines or integrating DICOM metadata into systems.

## Platforms
- Claude Desktop: Not Supported
- Claude Code: Supported (requires filesystem and code execution to read DICOM files)

## Instructions
1. Ask what the user wants to do: inspect header, extract metadata, read pixel data, anonymize PHI, convert to PNG/PNG stack, or modify attributes.
2. Confirm runtime environment and dependencies (Python version, pydicom, numpy, Pillow, gdcm or pylibjpeg for compressed pixel data).
3. Provide concise, ready-to-run Python snippets for common tasks: reading headers, extracting specific tags, saving pixel arrays to image files, anonymization patterns, and safe modification of tags while preserving required UIDs.
4. Include guidance for handling compressed DICOMs (installing decompression plugins), preserving modality-specific metadata, and recommendations for preserving auditability when anonymizing.
5. Offer troubleshooting tips for common errors (missing transfer syntax handlers, large pixel arrays), performance tips for large studies, and notes about DICOM conformance and legal requirements for PHI.
6. If requested, produce a small script template that reads a DICOM directory, anonymizes metadata per a user-specified profile, and outputs converted images or a CSV of metadata.

## Example Usage
- "Show pydicom code to anonymize patient names and IDs in a folder of DICOM files."
- "How do I convert a DICOM to a PNG using pydicom and Pillow?"
- "Give me a script to extract StudyDate, Modality, and SeriesDescription from all DICOMs in a directory."

## Note
Working with DICOM files often involves PHI; perform operations in secure environments and follow applicable privacy regulations. This skill requires running Python code and access to DICOM files.
