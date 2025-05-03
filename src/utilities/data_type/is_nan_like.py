from typing import Any

def is_nan_like(value: Any) -> bool:
    """
    Checks if a value is considered "Not a Number" or a common representation of a missing value.
    """
    if value is None:
        return True
    if isinstance(value, float):
        return value != value  # NaN check
    if isinstance(value, str):
        lower_value = value.strip().lower()
        return lower_value in ['', 'nan', 'none', 'null', '<na>']
    return False