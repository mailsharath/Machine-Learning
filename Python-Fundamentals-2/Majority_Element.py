def majority_element(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int32
    """
    dict1 = {}
    for i in range(len(nums)):
        if nums[i] in dict1.keys():
            dict1[nums[i]] += 1
        else:
            dict1[nums[i]] = 1
    for j, k in dict1.items():
        if k > len(nums)/2:
            return j# Write your code here.
    return 0