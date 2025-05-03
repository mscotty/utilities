import tarfile
import os
from typing import List, Literal

def create_tar_archive(output_filepath: str, input_paths: List[str], format: Literal['tar', 'gz', 'bz2'] = 'tar') -> None:
    """
    Creates a TAR archive (optionally compressed with gzip or bzip2)
    from a list of input files and/or directories.

    Args:
        output_filepath: The path to the TAR archive to be created (e.g., 'archive.tar', 'archive.tar.gz', 'archive.tar.bz2').
        input_paths: A list of file and/or directory paths to include.
        format: The format of the TAR archive ('tar', 'gz', 'bz2').
    """
    mode = 'w'
    if format == 'gz':
        mode += ':gz'
    elif format == 'bz2':
        mode += ':bz2'

    with tarfile.open(output_filepath, mode) as tf:
        for path in input_paths:
            if os.path.isfile(path):
                tf.add(path, arcname=os.path.basename(path))
            elif os.path.isdir(path):
                tf.add(path, arcname=os.path.basename(path), recursive=True)

def extract_tar_archive(tar_filepath: str, extract_dir: str) -> None:
    """
    Extracts all files and directories from a TAR archive.
    Automatically handles gzip and bzip2 compression based on the filename extension.

    Args:
        tar_filepath: The path to the TAR archive.
        extract_dir: The directory where the contents will be extracted.
    """
    os.makedirs(extract_dir, exist_ok=True)
    try:
        with tarfile.open(tar_filepath, 'r:*') as tf:
            tf.extractall(extract_dir)
    except tarfile.ReadError as e:
        print(f"Error reading TAR archive '{tar_filepath}': {e}")

def list_tar_contents(tar_filepath: str) -> List[str]:
    """
    Lists the names of all members (files and directories) within a TAR archive.
    Automatically handles gzip and bzip2 compression.

    Args:
        tar_filepath: The path to the TAR archive.

    Returns:
        A list of strings, where each string is the name of a member in the archive.
    """
    try:
        with tarfile.open(tar_filepath, 'r:*') as tf:
            return [member.name for member in tf.getmembers()]
    except tarfile.ReadError as e:
        print(f"Error reading TAR archive '{tar_filepath}': {e}")
        return []