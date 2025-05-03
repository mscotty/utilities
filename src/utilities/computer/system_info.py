import platform
import psutil
from datetime import datetime

def get_os_info() -> str:
    """Returns the operating system information."""
    return platform.system()

def get_python_version() -> str:
    """Returns the current Python version."""
    return platform.python_version()

def get_hostname() -> str:
    """Returns the system's hostname."""
    return platform.node()

def get_boot_time() -> datetime:
    """Returns the system boot time as a datetime object."""
    from datetime import datetime
    return datetime.fromtimestamp(psutil.boot_time())