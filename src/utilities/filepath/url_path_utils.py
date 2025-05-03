from urllib.parse import urlparse, urlunparse
import os

def path_to_url(filepath: str) -> str:
    """Converts a local filepath to a file URL."""
    return f"file://{os.path.abspath(filepath)}"

def url_to_path(file_url: str) -> str:
    """Converts a file URL to a local filepath."""
    parsed_url = urlparse(file_url)
    if parsed_url.scheme != "file":
        raise ValueError("Not a file URL")
    return os.path.normpath(parsed_url.path)

# More advanced functions could handle network paths or other URL schemes if needed.