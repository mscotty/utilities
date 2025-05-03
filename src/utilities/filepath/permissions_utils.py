import os
import stat
import platform

def get_file_permissions(filepath: str) -> str:
    """
    Returns the file permissions as a string (e.g., 'rwxr-xr--').
    Note: The format might vary slightly across operating systems.
    """
    mode = os.stat(filepath).st_mode
    return stat.filemode(mode)

def is_file_readable(filepath: str) -> bool:
    """Checks if the current user has read permissions for a file."""
    return os.access(filepath, os.R_OK)

def is_file_writable(filepath: str) -> bool:
    """Checks if the current user has write permissions for a file."""
    return os.access(filepath, os.W_OK)

def is_file_executable(filepath: str) -> bool:
    """Checks if the current user has execute permissions for a file."""
    return os.access(filepath, os.X_OK)

def set_file_permissions(filepath: str, mode: int) -> None:
    """
    Sets the file permissions using a numeric mode (e.g., 0o755).
    Requires appropriate permissions.
    """
    try:
        os.chmod(filepath, mode)
    except PermissionError:
        print(f"Permission denied to change permissions for '{filepath}'.")

# More advanced functions for setting specific user/group permissions
# might involve using the 'grp' and 'pwd' modules and might be OS-specific.