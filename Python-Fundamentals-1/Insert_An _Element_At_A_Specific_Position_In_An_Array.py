def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    """
    nums.pop()
    nums.insert(position-1, element)
    return nums


nums1 = [2, 4, 5, 6, -1]
element1 = 3
position1 = 2


print(insert_element_at_position(nums1, element1, position1))
