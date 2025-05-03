import yaml
from typing import Any

def read_yaml_file(filepath: str) -> Any:
    """Reads and parses a YAML file."""
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error reading YAML file '{filepath}': {e}")
        return None

def write_yaml_file(filepath: str, data: Any) -> None:
    """Writes data to a YAML file."""
    try:
        with open(filepath, 'w') as f:
            yaml.dump(data, f, indent=4)
    except yaml.YAMLError as e:
        print(f"Error writing YAML file '{filepath}': {e}")