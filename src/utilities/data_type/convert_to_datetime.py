from datetime import datetime
from typing import Union

def convert_to_datetime(value: Union[str, int, float], format_string: str = None) -> Union[datetime, None]:
    """
    Attempts to convert a value to a datetime object.

    Args:
        value: The value to convert (can be a string, integer timestamp, or float timestamp).
        format_string: An optional format string if the value is a string.

    Returns:
        A datetime object if conversion is successful, None otherwise.
    """
    if isinstance(value, str):
        if format_string:
            try:
                return datetime.strptime(value, format_string)
            except ValueError:
                return None
        else:
            formats_to_try = ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y", "%m/%d/%Y %H:%M:%S"]
            for fmt in formats_to_try:
                try:
                    return datetime.strptime(value, fmt)
                except ValueError:
                    continue
            return None
    elif isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(value)
        except ValueError:
            return None
    return None