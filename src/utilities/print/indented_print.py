def indented_print(text: str, level: int = 1, indent_char: str = "  ") -> None:
    """Prints text with a specified indentation level."""
    indentation = indent_char * level
    print(f"{indentation}{text}")

def print_header(text: str, level: int = 0, separator: str = "=" * 40) -> None:
    """Prints a header with an optional separator."""
    if level > 0:
        indented_print(separator, level=level - 1)
        indented_print(text.upper(), level=level)
        indented_print(separator, level=level - 1)
    else:
        print(separator)
        print(text.upper().center(len(separator)))
        print(separator)

# Example usage:
# print_header("Main Section")
# indented_print("Step 1: Initialize", level=1)
# indented_print("Sub-step A", level=2)
# indented_print("Step 2: Process data", level=1)
# print_header("Results", level=1, separator="-")