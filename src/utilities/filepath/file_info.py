import os
from datetime import datetime

def get_file_size_bytes(filepath: str) -> int:
    """Returns the size of a file in bytes."""
    return os.path.getsize(filepath)

def get_file_creation_time(filepath: str) -> datetime:
    """Returns the file creation time as a datetime object."""
    timestamp = os.path.getctime(filepath)
    return datetime.fromtimestamp(timestamp)

def get_file_modification_time(filepath: str) -> datetime:
    """Returns the file modification time as a datetime object."""
    timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp)

def check_file_exists(filepath: str) -> bool:
    """Checks if a file exists at the given path."""
    return os.path.isfile(filepath)

def check_directory_exists(path: str) -> bool:
    """Checks if a directory exists at the given path."""
    return os.path.isdir(path)