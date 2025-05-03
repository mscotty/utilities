import tempfile
import shutil
import os
from typing import Optional, TextIO

def create_temporary_file(suffix: Optional[str] = None, prefix: Optional[str] = None, dir: Optional[str] = None, text: bool = False) -> TextIO:
    """Creates a temporary file and returns the file object."""
    return tempfile.NamedTemporaryFile(suffix=suffix, prefix=prefix, dir=dir, delete=False, mode='w+' if text else 'wb+')

def create_temporary_directory(suffix: Optional[str] = None, prefix: Optional[str] = None, dir: Optional[str] = None) -> str:
    """Creates a temporary directory and returns its path."""
    return tempfile.mkdtemp(suffix=suffix, prefix=prefix, dir=dir)

def cleanup_temporary_path(path: str) -> None:
    """Deletes a temporary file or directory."""
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)