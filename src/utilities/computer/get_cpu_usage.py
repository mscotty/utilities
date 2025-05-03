import psutil

def get_cpu_percentage(interval: float = 0.1) -> float:
    """Returns the system-wide CPU utilization as a percentage."""
    return psutil.cpu_percent(interval=interval)

def get_per_cpu_percentage(interval: float = 0.1) -> list[float]:
    """Returns a list representing the utilization percentage of each CPU core."""
    return psutil.cpu_percent(interval=interval, percpu=True)