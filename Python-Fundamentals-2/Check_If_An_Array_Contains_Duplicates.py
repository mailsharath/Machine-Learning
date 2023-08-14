def check_if_array_contains_duplicate(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     bool
    """
    unique_items = []
    for item in nums:
        if item in unique_items:
            return True
        else:
            unique_items.append(item)
    return False
