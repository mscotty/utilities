import psutil

def get_process_list() -> list[psutil.Process]:
    """Returns a list of all running processes."""
    return list(psutil.process_iter())

def find_processes_by_name(process_name: str) -> list[psutil.Process]:
    """Finds and returns a list of processes by their name."""
    return [proc for proc in psutil.process_iter(['name']) if proc.info['name'].lower() == process_name.lower()]

# def kill_process_by_pid(pid: int) -> None: # Be very careful with this!
#     """Kills a process given its process ID."""
#     try:
#         process = psutil.Process(pid)
#         process.kill()
#     except psutil.NoSuchProcess:
#         print(f"Process with PID {pid} not found.")

# ... more advanced process management utilities