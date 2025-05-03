import os
import psutil

def get_process_priority(pid: int) -> int:
    """
    Gets the priority of a process given its PID.
    Lower values typically indicate higher priority (platform-dependent).
    """
    try:
        process = psutil.Process(pid)
        return process.nice()
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        return None

def set_process_priority(pid: int, priority: int) -> bool:
    """
    Sets the priority (niceness) of a process given its PID.
    The range of nice values is typically from -20 (highest priority) to 19 (lowest priority).
    Requires appropriate permissions.
    """
    try:
        process = psutil.Process(pid)
        process.nice(priority)
        return True
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        return False
    except psutil.AccessDenied:
        print(f"Permission denied to set priority for PID {pid}.")
        return False

# Example usage:
# current_priority = get_process_priority(os.getpid())
# print(f"Current process priority: {current_priority}")
# set_process_priority(os.getpid(), -5) # Attempt to increase priority