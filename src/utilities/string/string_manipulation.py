def reverse_string(text: str) -> str:
    """Reverses a string."""
    return text[::-1]

def remove_prefix(text: str, prefix: str) -> str:
    """Removes a prefix from a string if it exists."""
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def remove_suffix(text: str, suffix: str) -> str:
    """Removes a suffix from a string if it exists."""
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text

def replace_multiple(text: str, replacements: dict[str, str]) -> str:
    """Performs multiple string replacements based on a dictionary."""
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def capitalize_first_letter(text: str) -> str:
    """Capitalizes the first letter of a string."""
    return text[0].upper() + text[1:] if text else text

# Example usage:
# print(reverse_string("hello"))
# print(remove_prefix("prefix_example", "prefix_"))
# replacements = {"apple": "orange", "banana": "grape"}
# print(replace_multiple("I like apple and banana.", replacements))
# print(capitalize_first_letter("world"))