# Requirements: Smart Downloads Organizer

## Overview
A command-line Python script that automatically organizes files in a folder (default: Downloads) into categorized subfolders based on file type.

## Functional Requirements

### FR1: Folder Selection
- The script shall prompt the user for a folder path
- If the user presses Enter without input, use the default Downloads folder
- The script shall validate that the folder exists

### FR2: File Categorization
- The script shall categorize files by extension into:
  - **Images**: jpg, jpeg, png, gif, bmp, svg, webp
  - **Documents**: pdf, doc, docx, txt, ppt, xls, xlsx
  - **Videos**: mp4, mkv, avi, mov, webm
  - **Audio**: mp3, wav, m4a, flac
  - **Archives**: zip, rar, 7z, tar, gz
  - **Others**: all other file types
- The script shall only process files, not subdirectories

### FR3: Folder Organization
- The script shall create category subfolders if they don't exist
- The script shall move files into their respective category folders
- If a file with the same name exists in the target folder:
  - The script shall rename the file being moved (e.g., file_1.txt, file_2.txt)

### FR4: Summary Report
- The script shall print a summary showing:
  - Number of files moved to each category
  - Example: "Moved 5 files to Images, 3 to Documents, 2 to Videos, 1 to Others."

### FR5: Error Handling
- The script shall handle errors gracefully without crashing
- The script shall print friendly error messages for:
  - Invalid folder paths
  - Permission errors
  - File operation failures

## Non-Functional Requirements

### NFR1: Technology
- Use Python 3 (standard library only, no external dependencies)
- Command-line interface only

### NFR2: Code Structure
- Main file: `organize_downloads.py`
- Include clear function structure:
  - `get_downloads_folder()`
  - `categorize_file(filename)`
  - `organize_folder(path)`

### NFR3: Documentation
- Include `README.md` with usage instructions
- Include `requirements.txt` (empty or with standard library comment)

## Acceptance Criteria

- AC1: User can run the script and organize their Downloads folder
- AC2: User can specify a custom folder path
- AC3: Files are correctly categorized and moved
- AC4: No files are lost or overwritten
- AC5: Summary is displayed after organization
- AC6: Script handles errors without crashing
