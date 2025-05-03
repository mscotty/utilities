import tempfile
from typing import Optional

def generate_temporary_filepath(suffix: Optional[str] = None, prefix: Optional[str] = None, dir: Optional[str] = None) -> str:
    """Generates a unique temporary filepath without creating the file."""
    return tempfile.mktemp(suffix=suffix, prefix=prefix, dir=dir)

def generate_temporary_directorypath(suffix: Optional[str] = None, prefix: Optional[str] = None, dir: Optional[str] = None) -> str:
    """Generates a unique temporary directory path without creating the directory."""
    return tempfile.mkdtemp(suffix=suffix, prefix=prefix, dir=dir)