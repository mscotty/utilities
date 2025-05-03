from typing import Any, Type, Optional

def safe_cast(value: Any, target_type: Type) -> Optional[Any]:
    """
    Safely casts a value to a target type, returning None if the cast fails.
    """
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return None

# Example usage:
# integer_value = safe_cast("123", int)  # Returns 123
# float_value = safe_cast("abc", float)  # Returns None