import re

def snake_case_to_camel_case(snake_str: str) -> str:
    """Converts a snake_case string to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_case_to_snake_case(camel_str: str) -> str:
    """Converts a camelCase string to snake_case."""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()

def remove_non_alphanumeric(text: str) -> str:
    """Removes all non-alphanumeric characters from a string."""
    return re.sub(r'[^a-zA-Z0-9]', '', text)