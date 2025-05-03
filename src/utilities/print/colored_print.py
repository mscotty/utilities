class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colored_text(text: str, color: str = Colors.RESET, bold: bool = False, underline: bool = False) -> str:
    """Applies color, bold, and underline formatting to text."""
    style = color
    if bold:
        style += Colors.BOLD
    if underline:
        style += Colors.UNDERLINE
    return f"{style}{text}{Colors.RESET}"

def print_info(text: str) -> None:
    """Prints informational text in blue."""
    print(colored_text(f"INFO: {text}", Colors.BLUE))

def print_warning(text: str) -> None:
    """Prints warning text in yellow."""
    print(colored_text(f"WARNING: {text}", Colors.YELLOW))

def print_error(text: str) -> None:
    """Prints error text in red and bold."""
    print(colored_text(f"ERROR: {text}", Colors.RED, bold=True))

def print_success(text: str) -> None:
    """Prints success text in green."""
    print(colored_text(f"SUCCESS: {text}", Colors.GREEN))

# Example usage:
# print(colored_text("Hello", Colors.RED, bold=True))
# print_info("Operation started.")
# print_warning("Configuration file not found.")
# print_error("An unexpected error occurred!")
# print_success("Task completed successfully.")