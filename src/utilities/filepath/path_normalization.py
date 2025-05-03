import os

def normalize_case(filepath: str) -> str:
    """Normalizes the case of a filepath to the standard for the operating system."""
    return os.path.normcase(filepath)

def are_paths_equal(path1: str, path2: str, case_sensitive: bool = True) -> bool:
    """Compares two paths for equality, with optional case sensitivity."""
    normalized_path1 = os.path.normpath(path1)
    normalized_path2 = os.path.normpath(path2)
    if case_sensitive:
        return normalized_path1 == normalized_path2
    else:
        return os.path.normcase(normalized_path1) == os.path.normcase(normalized_path2)

def resolve_path_relative_to(base_path: str, relative_path: str) -> str:
    """Resolves a relative path against a given base path."""
    return os.path.abspath(os.path.join(base_path, relative_path))