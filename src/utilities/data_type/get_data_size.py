import sys
from typing import Any

def get_data_size_bytes(data: Any) -> int:
    """
    Returns the size of an object in bytes.
    Note that this is a shallow size and might not reflect the total memory usage
    of complex objects and their references.
    """
    return sys.getsizeof(data)