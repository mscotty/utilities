import os
import psutil

def get_process_affinity(pid: int) -> list[int]:
    """
    Gets the CPU affinity of a process given its PID.
    Returns a list of CPU cores the process is allowed to run on.
    """
    try:
        process = psutil.Process(pid)
        return process.cpu_affinity()
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        return None

def set_process_affinity(pid: int, cpu_list: list[int]) -> bool:
    """
    Sets the CPU affinity of a process given its PID to a list of CPU cores.
    """
    try:
        process = psutil.Process(pid)
        process.cpu_affinity(cpu_list)
        return True
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        return False
    except ValueError:
        print(f"Invalid CPU core specified in the list for PID {pid}.")
        return False
    except psutil.AccessDenied:
        print(f"Permission denied to set CPU affinity for PID {pid}.")
        return False

def get_available_cpu_cores() -> list[int]:
    """Returns a list of available logical CPU cores."""
    return list(range(os.cpu_count()))

# Example usage:
# current_affinity = get_process_affinity(os.getpid())
# print(f"Current process affinity: {current_affinity}")
# available_cores = get_available_cpu_cores()
# if available_cores:
#     set_process_affinity(os.getpid(), [available_cores[0]]) # Pin to the first core