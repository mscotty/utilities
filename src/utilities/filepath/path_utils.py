import os

def create_directory_if_not_exists(path: str) -> None:
    """Creates a directory at the given path if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def get_file_extension(filepath: str) -> str:
    """Extracts the extension from a file path."""
    _, extension = os.path.splitext(filepath)
    return extension.lstrip('.')

def list_files_with_extension(directory: str, extension: str) -> list[str]:
    """Lists all files in a directory with a specific extension."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(f'.{extension}')]
