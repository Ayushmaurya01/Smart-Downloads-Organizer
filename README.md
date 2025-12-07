# Smart Downloads Organizer

A Python command-line tool that automatically organizes files in your Downloads folder (or any folder) into categorized subfolders based on file type.

## Features

- 📁 Automatically categorizes files by extension
- 🎨 Organizes into: Images, Documents, Videos, Audio, Archives, and Others
- 🔄 Handles name conflicts by renaming duplicates
- 📊 Provides a summary report after organization
- ⚡ No external dependencies required

## Categories

- **Images**: jpg, jpeg, png, gif, bmp, svg, webp
- **Documents**: pdf, doc, docx, txt, ppt, xls, xlsx
- **Videos**: mp4, mkv, avi, mov, webm
- **Audio**: mp3, wav, m4a, flac
- **Archives**: zip, rar, 7z, tar, gz
- **Others**: everything else

## Installation

No installation required! Just Python 3.6 or higher.

```bash
# Clone or download this repository
# Navigate to the project directory
```

## Usage

### Basic Usage (Default Downloads Folder)

```bash
python organize_downloads.py
```

When prompted, just press Enter to use your default Downloads folder.

### Custom Folder

```bash
python organize_downloads.py
```

When prompted, enter the full path to the folder you want to organize:
```
> C:\Users\YourName\Desktop\MessyFolder
```

or on macOS/Linux:
```
> /Users/YourName/Desktop/MessyFolder
```

## Example Output

```
==================================================
Smart Downloads Organizer
==================================================

Enter folder path to organize
(or press Enter for Downloads folder):
> 

Using default: C:\Users\YourName\Downloads

Organizing files in: C:\Users\YourName\Downloads
--------------------------------------------------
✓ vacation.jpg → Images
✓ report.pdf → Documents
✓ movie.mp4 → Videos
✓ song.mp3 → Audio
✓ archive.zip → Archives
✓ readme.txt → Documents

==================================================
Organization complete!
==================================================
Moved 1 file to Images
Moved 2 files to Documents
Moved 1 file to Videos
Moved 1 file to Audio
Moved 1 file to Archives

Total: 6 files organized
```

## Safety Features

- **No Overwriting**: If a file with the same name exists in the target folder, the script automatically renames it (e.g., `file_1.txt`, `file_2.txt`)
- **Error Handling**: Gracefully handles permission errors and continues processing other files
- **Non-Destructive**: Only moves files, never deletes them

## Requirements

- Python 3.6 or higher
- Standard library only (no pip install needed)

## Project Structure

```
.
├── organize_downloads.py  # Main script
├── README.md             # This file
├── requirements.txt      # Dependencies (empty - stdlib only)
├── requirements.md       # Project requirements
└── design.md            # Design documentation
```

## Troubleshooting

**Permission Denied Error**
- Make sure you have read/write permissions for the folder
- Try running as administrator (Windows) or with sudo (macOS/Linux)

**Folder Not Found**
- Double-check the folder path
- Use absolute paths for best results
- On Windows, use forward slashes (/) or double backslashes (\\\\)

## License

Free to use and modify as needed.
