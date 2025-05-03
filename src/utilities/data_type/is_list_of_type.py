from typing import Type

def is_list_of_type(data: list, expected_type: Type) -> bool:
    """
    Checks if a list contains only elements of a specific type.
    """
    if not isinstance(data, list):
        return False
    return all(isinstance(item, expected_type) for item in data)