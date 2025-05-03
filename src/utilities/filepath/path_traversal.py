import os
from typing import List, Callable

def get_files_recursively(root_dir: str, filter_func: Optional[Callable[[str], bool]] = None) -> List[str]:
    """
    Recursively gets all filepaths under a given root directory,
    optionally filtered by a function.
    """
    file_paths = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            filepath = os.path.join(root, file)
            if filter_func is None or filter_func(filepath):
                file_paths.append(filepath)
    return file_paths

def get_directories_recursively(root_dir: str, filter_func: Optional[Callable[[str], bool]] = None) -> List[str]:
    """
    Recursively gets all directory paths under a given root directory,
    optionally filtered by a function.
    """
    dir_paths = []
    for root, dirs, _ in os.walk(root_dir):
        for dir_name in dirs:
            dirpath = os.path.join(root, dir_name)
            if filter_func is None or filter_func(dirpath):
                dir_paths.append(dirpath)
    return dir_paths