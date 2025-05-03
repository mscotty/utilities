from typing import Type, Dict

def is_dict_with_types(data: Dict, key_type: Type, value_type: Type) -> bool:
    """
    Checks if a dictionary contains keys of a specific type and values of another specific type.
    """
    if not isinstance(data, dict):
        return False
    return all(isinstance(key, key_type) and isinstance(value, value_type) for key, value in data.items())