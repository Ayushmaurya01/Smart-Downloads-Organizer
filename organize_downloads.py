#!/usr/bin/env python3
"""
Smart Downloads Organizer
Automatically organizes files in a folder into categorized subfolders.
"""

import os
import shutil
from pathlib import Path

# Category mappings
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.xls', '.xlsx'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.webm'],
    'Audio': ['.mp3', '.wav', '.m4a', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
}


def get_downloads_folder():
    """Get the path to the user's Downloads folder."""
    return Path.home() / "Downloads"


def categorize_file(filename):
    """
    Categorize a file based on its extension.
    
    Args:
        filename: Name of the file
        
    Returns:
        Category name (string)
    """
    extension = Path(filename).suffix.lower()
    
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    
    return 'Others'


def get_unique_filename(target_dir, filename):
    """
    Generate a unique filename if a file with the same name exists.
    
    Args:
        target_dir: Target directory path
        filename: Original filename
        
    Returns:
        Unique filename
    """
    target_path = target_dir / filename
    
    if not target_path.exists():
        return filename
    
    # File exists, generate unique name
    stem = target_path.stem
    suffix = target_path.suffix
    counter = 1
    
    while True:
        new_filename = f"{stem}_{counter}{suffix}"
        new_path = target_dir / new_filename
        if not new_path.exists():
            return new_filename
        counter += 1


def organize_folder(folder_path):
    """
    Organize files in the specified folder into categorized subfolders.
    
    Args:
        folder_path: Path to the folder to organize
        
    Returns:
        Dictionary with counts of files moved per category
    """
    folder = Path(folder_path)
    
    # Validate folder exists
    if not folder.exists():
        print(f"Error: Folder '{folder_path}' does not exist.")
        return None
    
    if not folder.is_dir():
        print(f"Error: '{folder_path}' is not a directory.")
        return None
    
    print(f"\nOrganizing files in: {folder}")
    print("-" * 50)
    
    # Statistics
    stats = {category: 0 for category in CATEGORIES.keys()}
    stats['Others'] = 0
    
    # Get all files (not directories) in the folder
    try:
        files = [f for f in folder.iterdir() if f.is_file()]
    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")
        return None
    
    if not files:
        print("No files found to organize.")
        return stats
    
    # Process each file
    for file_path in files:
        try:
            # Determine category
            category = categorize_file(file_path.name)
            
            # Create category folder if it doesn't exist
            category_folder = folder / category
            category_folder.mkdir(exist_ok=True)
            
            # Get unique filename to avoid overwriting
            unique_filename = get_unique_filename(category_folder, file_path.name)
            target_path = category_folder / unique_filename
            
            # Move the file
            shutil.move(str(file_path), str(target_path))
            
            # Update statistics
            stats[category] += 1
            
            # Print progress
            display_name = file_path.name
            if len(display_name) > 40:
                display_name = display_name[:37] + "..."
            print(f"✓ {display_name} → {category}")
            
        except PermissionError:
            print(f"✗ Permission denied: {file_path.name}")
        except Exception as e:
            print(f"✗ Error moving {file_path.name}: {str(e)}")
    
    return stats


def print_summary(stats):
    """
    Print a summary of the organization results.
    
    Args:
        stats: Dictionary with counts per category
    """
    print("\n" + "=" * 50)
    print("Organization complete!")
    print("=" * 50)
    
    total = 0
    summary_parts = []
    
    for category, count in stats.items():
        if count > 0:
            total += count
            file_word = "file" if count == 1 else "files"
            summary_parts.append(f"Moved {count} {file_word} to {category}")
    
    if summary_parts:
        for part in summary_parts:
            print(part)
        print(f"\nTotal: {total} files organized")
    else:
        print("No files were moved.")


def main():
    """Main entry point for the script."""
    print("=" * 50)
    print("Smart Downloads Organizer")
    print("=" * 50)
    
    # Get folder path from user
    default_folder = get_downloads_folder()
    user_input = input(f"\nEnter folder path to organize\n(or press Enter for Downloads folder):\n> ").strip()
    
    if user_input:
        folder_path = user_input
    else:
        folder_path = default_folder
        print(f"Using default: {folder_path}")
    
    # Organize the folder
    stats = organize_folder(folder_path)
    
    # Print summary if successful
    if stats is not None:
        print_summary(stats)


if __name__ == "__main__":
    main()
