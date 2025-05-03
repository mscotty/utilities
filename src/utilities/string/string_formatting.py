def center_string(text: str, width: int, fillchar: str = ' ') -> str:
    """Centers a string within a specified width using a fill character."""
    return text.center(width, fillchar)

def left_pad_string(text: str, width: int, fillchar: str = ' ') -> str:
    """Left-pads a string to a specified width using a fill character."""
    return text.ljust(width, fillchar)

def right_pad_string(text: str, width: int, fillchar: str = ' ') -> str:
    """Right-pads a string to a specified width using a fill character."""
    return text.rjust(width, fillchar)

def truncate_string(text: str, max_length: int, ellipsis: str = '...') -> str:
    """Truncates a string to a maximum length, adding an ellipsis if needed."""
    if len(text) > max_length:
        return text[:max_length - len(ellipsis)] + ellipsis
    return text

def wrap_text(text: str, width: int) -> str:
    """Wraps text to a specified width, breaking words if necessary."""
    import textwrap
    return textwrap.fill(text, width=width)

# Example usage:
# print(center_string("Hello", 20, "*"))
# print(left_pad_string("World", 15, "-"))
# print(truncate_string("This is a very long string that needs to be shortened.", 20))
# print(wrap_text("This is a long sentence that should be wrapped to a certain width for better readability.", 30))