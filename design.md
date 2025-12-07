# Design: Smart Downloads Organizer

## Architecture

### High-Level Design
```
User Input → Folder Validation → File Scanning → Categorization → File Moving → Summary Report
```

### Component Design

#### 1. Main Entry Point
- Function: `main()`
- Responsibilities:
  - Orchestrate the entire workflow
  - Handle user input
  - Call organize_folder()
  - Display results

#### 2. Downloads Folder Detection
- Function: `get_downloads_folder()`
- Returns: Path to the user's Downloads folder
- Platform support: Windows, macOS, Linux
- Implementation:
  - Use `pathlib.Path.home()` to get user home directory
  - Append "Downloads" to the path

#### 3. File Categorization
- Function: `categorize_file(filename)`
- Input: filename (string)
- Returns: category name (string)
- Logic:
  - Extract file extension (lowercase)
  - Match against predefined category mappings
  - Return "Others" if no match

#### 4. File Organization
- Function: `organize_folder(path)`
- Input: folder path (string)
- Returns: dictionary with move counts per category
- Logic:
  - Validate folder exists
  - Scan for files (ignore subdirectories)
  - For each file:
    - Determine category
    - Create category subfolder if needed
    - Handle name conflicts
    - Move file
    - Track statistics
  - Return statistics

#### 5. Name Conflict Resolution
- Function: `get_unique_filename(target_dir, filename)`
- Input: target directory, filename
- Returns: unique filename
- Logic:
  - If file doesn't exist, return original name
  - If exists, append counter: file_1.ext, file_2.ext, etc.

## Data Structures

### Category Mappings
```python
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.webm'],
    'Audio': ['.mp3', '.wav', '.m4a', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
}
```

### Statistics Dictionary
```python
{
    'Images': 5,
    'Documents': 3,
    'Videos': 2,
    'Audio': 0,
    'Archives': 1,
    'Others': 1
}
```

## Error Handling

### Error Scenarios
1. **Invalid folder path**: Print error and exit gracefully
2. **Permission denied**: Print error for specific file and continue
3. **File move failure**: Print error and continue with next file
4. **Unexpected errors**: Catch general exceptions, print message, continue

### Error Messages
- User-friendly, non-technical language
- Include context (which file, what operation)
- Suggest possible solutions when applicable

## User Interface

### Input Prompt
```
Enter folder path to organize (or press Enter for Downloads folder):
```

### Progress Indication
```
Organizing files in: /path/to/folder
Processing: file1.jpg → Images
Processing: document.pdf → Documents
...
```

### Summary Output
```
Organization complete!
Moved 5 files to Images
Moved 3 files to Documents
Moved 2 files to Videos
Moved 1 file to Others
Total: 11 files organized
```

## Testing Strategy

### Manual Testing
1. Create test folder with sample files
2. Run script on test folder
3. Verify:
   - Correct categorization
   - Proper folder creation
   - Name conflict handling
   - Summary accuracy

### Edge Cases
- Empty folder
- Folder with only subdirectories
- Files without extensions
- Files with multiple dots in name
- Very long filenames
