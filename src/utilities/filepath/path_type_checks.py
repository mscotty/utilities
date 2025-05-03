import os

def is_absolute_path(path: str) -> bool:
    """Checks if a path is an absolute path."""
    return os.path.isabs(path)

def is_relative_path(path: str) -> bool:
    """Checks if a path is a relative path."""
    return not os.path.isabs(path)

def is_valid_path(path: str) -> bool:
    """Performs a basic check to see if a path string is likely valid (doesn't check existence)."""
    return isinstance(path, str) and path.strip() != ""

# More advanced validation might involve checking for illegal characters
# based on the operating system.