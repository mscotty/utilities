import os
from typing import Optional

def create_symlink(src: str, dst: str, overwrite: bool = False) -> None:
    """
    Creates a symbolic link.

    Args:
        src: The path to the target file or directory.
        dst: The path where the symbolic link will be created.
        overwrite: If True, overwrites the destination if it already exists.
                   Use with caution!
    """
    if overwrite and os.path.exists(dst):
        os.remove(dst)
    try:
        os.symlink(src, dst)
    except OSError as e:
        print(f"Error creating symlink: {e}")

def read_symlink(path: str) -> Optional[str]:
    """Reads the target of a symbolic link."""
    if os.path.islink(path):
        return os.readlink(path)
    return None

def is_symlink(path: str) -> bool:
    """Checks if a path is a symbolic link."""
    return os.path.islink(path)

def resolve_symlink(path: str) -> str:
    """Resolves a symbolic link to its target path."""
    return os.path.realpath(path)