import resource

def get_soft_and_hard_limits(resource_name: int) -> tuple[int, int]:
    """
    Retrieves the soft and hard limits for a given resource.

    Args:
        resource_name: An integer constant from the `resource` module
                       (e.g., `resource.RLIMIT_CPU`, `resource.RLIMIT_NOFILE`).

    Returns:
        A tuple containing the soft limit and the hard limit.
    """
    return resource.getrlimit(resource_name)

def set_soft_limit(resource_name: int, new_soft_limit: int) -> None:
    """
    Sets the soft limit for a given resource. The new soft limit
    cannot exceed the existing hard limit.

    Args:
        resource_name: An integer constant from the `resource` module.
        new_soft_limit: The new soft limit value.
    """
    soft, hard = resource.getrlimit(resource_name)
    resource.setrlimit(resource_name, (new_soft_limit, hard))

# Add similar functions for setting hard limits with appropriate warnings,
# as increasing hard limits might require special privileges.

# Example usage:
# cpu_limits = get_soft_and_hard_limits(resource.RLIMIT_CPU)
# print(f"CPU Soft Limit: {cpu_limits[0]}, Hard Limit: {cpu_limits[1]}")