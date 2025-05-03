from typing import Any

def is_empty(value: Any) -> bool:
    """
    Checks if a value is considered empty or blank.
    Handles various data types like strings, lists, dictionaries, and None.
    """
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, set, dict)):
        return not value
    return False