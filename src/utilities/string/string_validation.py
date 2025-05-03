def is_empty_or_whitespace(text: str) -> bool:
    """Checks if a string is empty or contains only whitespace."""
    return not text.strip()

def contains_only_digits(text: str) -> bool:
    """Checks if a string contains only digits."""
    return text.isdigit()

def contains_only_alphabetic(text: str) -> bool:
    """Checks if a string contains only alphabetic characters."""
    return text.isalpha()

def contains_alphanumeric(text: str) -> bool:
    """Checks if a string contains at least one alphanumeric character."""
    return any(c.isalnum() for c in text)

def starts_with(text: str, prefix: str) -> bool:
    """Checks if a string starts with a given prefix."""
    return text.startswith(prefix)

def ends_with(text: str, suffix: str) -> bool:
    """Checks if a string ends with a given suffix."""
    return text.endswith(suffix)

# Example usage:
# print(is_empty_or_whitespace("  \n "))
# print(contains_only_digits("12345"))
# print(contains_only_alphabetic("HelloWorld"))
# print(starts_with("filename.txt", "file"))