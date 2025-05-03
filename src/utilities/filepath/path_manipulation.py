import os
import shutil
from typing import List

def create_directory(path: str, exist_ok: bool = False) -> None:
    """Creates a directory at the given path. Raises FileExistsError if the directory already exists and exist_ok is False."""
    os.makedirs(path, exist_ok=exist_ok)

def delete_directory(path: str, ignore_errors: bool = False, onerror=None) -> None:
    """Deletes a directory and all its contents."""
    shutil.rmtree(path, ignore_errors=ignore_errors, onerror=onerror)

def copy_file(src: str, dst: str, follow_symlinks: bool = True) -> str:
    """Copies a file from source to destination."""
    return shutil.copy2(src, dst, follow_symlinks=follow_symlinks) # copy2 preserves metadata

def move_file_or_directory(src: str, dst: str) -> str:
    """Moves a file or directory from source to destination."""
    return shutil.move(src, dst)

def list_subdirectories(directory: str) -> List[str]:
    """Lists all subdirectories within a given directory."""
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def join_paths(*args: str) -> str:
    """Joins multiple path components intelligently."""
    return os.path.join(*args)

def normalize_path(path: str) -> str:
    """Normalizes a path, making it absolute and canonical."""
    return os.path.abspath(os.path.realpath(path))