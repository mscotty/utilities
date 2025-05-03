from datetime import datetime

def is_datetime(value: str, format_string: str = None) -> bool:
    """
    Checks if a string can be parsed as a datetime object.

    Args:
        value: The string to check.
        format_string: An optional format string to use for parsing.
                       If None, it will try a few common formats.

    Returns:
        True if the string can be parsed as a datetime, False otherwise.
    """
    if not isinstance(value, str):
        return False
    if format_string:
        try:
            datetime.strptime(value, format_string)
            return True
        except ValueError:
            return False
    else:
        formats_to_try = ["%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y", "%m/%d/%Y %H:%M:%S"]
        for fmt in formats_to_try:
            try:
                datetime.strptime(value, fmt)
                return True
            except ValueError:
                continue
        return False