def is_bool(value: any) -> bool:
    """
    Checks if a value can be interpreted as a boolean (True or False).
    Considers common string representations as well.
    """
    if isinstance(value, bool):
        return True
    if isinstance(value, str):
        lower_value = value.lower()
        return lower_value in ['true', 'false', '1', '0', 'yes', 'no']
    if isinstance(value, int):
        return value in [0, 1]
    return False

def convert_to_bool(value: any) -> Union[bool, None]:
    """
    Attempts to convert a value to a boolean.
    Considers common string and integer representations.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lower_value = value.lower()
        if lower_value in ['true', '1', 'yes']:
            return True
        elif lower_value in ['false', '0', 'no']:
            return False
        else:
            return None
    if isinstance(value, int):
        if value == 1:
            return True
        elif value == 0:
            return False
        else:
            return None
    return None