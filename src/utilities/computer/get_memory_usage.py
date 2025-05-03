import psutil

def get_total_memory_gb() -> float:
    """Returns the total system memory in gigabytes."""
    return psutil.virtual_memory().total / (1024 ** 3)

def get_available_memory_gb() -> float:
    """Returns the available system memory in gigabytes."""
    return psutil.virtual_memory().available / (1024 ** 3)

def get_memory_usage_percent() -> float:
    """Returns the system memory usage as a percentage."""
    return psutil.virtual_memory().percent

def get_memory_usage_details() -> psutil._common.svmem:
    """Returns detailed memory usage statistics as a named tuple."""
    return psutil.virtual_memory()