def contains_duplicate(nums):
    unique_items = []
    for item in nums:
        if item in unique_items:
            return True
        else:
            unique_items.append(item)
    return False


nums1 = [1, 1, 2, 3, 4, 5]
print(contains_duplicate(nums1))
