import os
from typing import List, Optional

def get_filename(filepath: str) -> str:
    """Returns the base filename from a path (e.g., 'my_document.txt')."""
    return os.path.basename(filepath)

def get_filename_without_extension(filepath: str) -> str:
    """Returns the filename without its extension (e.g., 'my_document')."""
    name, _ = os.path.splitext(os.path.basename(filepath))
    return name

def get_directory(filepath: str) -> str:
    """Returns the directory part of a path (e.g., '/path/to')."""
    return os.path.dirname(filepath)

def split_path(filepath: str) -> List[str]:
    """Splits a path into its individual components."""
    return filepath.split(os.sep)

def join_path_components(components: List[str]) -> str:
    """Joins a list of path components into a full path."""
    return os.path.join(*components)

def change_file_extension(filepath: str, new_extension: str) -> str:
    """Changes the extension of a file path."""
    name, _ = os.path.splitext(filepath)
    return name + (f".{new_extension}" if new_extension else "")

def append_suffix_to_filename(filepath: str, suffix: str) -> str:
    """Appends a suffix to the filename (before the extension, if any)."""
    name, ext = os.path.splitext(filepath)
    return f"{name}{suffix}{ext}"