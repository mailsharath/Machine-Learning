def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    l, r = 0, len(nums)-1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


nums1 = [1, 2, 3, 4, 5, 6]

print(reverse_array(nums1))

