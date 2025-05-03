import json
from typing import Any

def read_json_file(filepath: str) -> Any:
    """Reads and parses a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json_file(filepath: str, data: Any) -> None:
    """Writes data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)