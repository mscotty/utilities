import zipfile
import os
from typing import List

def create_zip_archive(output_filepath: str, input_paths: List[str], compress_type=zipfile.ZIP_DEFLATED) -> None:
    """
    Creates a ZIP archive from a list of input files and/or directories.

    Args:
        output_filepath: The path to the ZIP archive to be created.
        input_paths: A list of file and/or directory paths to include in the archive.
        compress_type: The compression method to use (e.g., zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED).
    """
    with zipfile.ZipFile(output_filepath, 'w', compress_type) as zf:
        for path in input_paths:
            if os.path.isfile(path):
                zf.write(path, os.path.basename(path))
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        relative_path = os.path.relpath(file_path, os.path.dirname(path))
                        zf.write(file_path, os.path.join(os.path.basename(path), relative_path))

def extract_zip_archive(zip_filepath: str, extract_dir: str) -> None:
    """
    Extracts all files and directories from a ZIP archive to a specified directory.

    Args:
        zip_filepath: The path to the ZIP archive.
        extract_dir: The directory where the contents will be extracted.
    """
    os.makedirs(extract_dir, exist_ok=True)
    with zipfile.ZipFile(zip_filepath, 'r') as zf:
        zf.extractall(extract_dir)

def list_zip_contents(zip_filepath: str) -> List[str]:
    """
    Lists the names of all files and directories within a ZIP archive.

    Args:
        zip_filepath: The path to the ZIP archive.

    Returns:
        A list of strings, where each string is the name of an item in the archive.
    """
    with zipfile.ZipFile(zip_filepath, 'r') as zf:
        return zf.namelist()