def get_user_input(prompt: str, default: Optional[str] = None) -> str:
    """Prompts the user for input and returns the response."""
    if default is not None:
        return input(f"{prompt} (default: {default}): ") or default
    else:
        return input(f"{prompt}: ")

def confirm_action(prompt: str, default: bool = False) -> bool:
    """Prompts the user for confirmation (yes/no)."""
    choices = ' [Y/n] ' if default else ' [y/N] '
    response = input(prompt + choices).lower().strip()
    if default:
        return response not in ['n', 'no']
    else:
        return response in ['y', 'yes']

# Example usage:
# name = get_user_input("Enter your name")
# print(f"Hello, {name}!")
# continue_processing = confirm_action("Do you want to continue?")
# if continue_processing:
#     print("Continuing...")
# else:
#     print("Aborting.")
# file_path = get_user_input("Enter the output file path", default="output.txt")
# print(f"Output will be saved to: {file_path}")