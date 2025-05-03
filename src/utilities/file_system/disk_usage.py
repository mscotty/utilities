import shutil

def get_disk_usage(path: str) -> tuple[int, int, int]:
    """
    Returns disk usage statistics for the given path.

    Args:
        path: The path to a file or directory.

    Returns:
        A tuple containing (total, used, free) space in bytes.
    """
    total, used, free = shutil.disk_usage(path)
    return total, used, free

def format_disk_usage(total: int, used: int, free: int) -> str:
    """Formats disk usage in a human-readable string."""
    def convert_bytes(bytes_val):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.1f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.1f} PB"

    total_str = convert_bytes(total)
    used_str = convert_bytes(used)
    free_str = convert_bytes(free)
    return f"Total: {total_str}, Used: {used_str}, Free: {free_str}"

# Example usage:
# total, used, free = get_disk_usage(".")
# print(format_disk_usage(total, used, free))