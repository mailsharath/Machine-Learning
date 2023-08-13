def intersection_of_arrays(nums1, nums2):
    intersection = []
    for item in nums1:
        if item in nums2:
            if item not in intersection:
                intersection.append(item)
    return intersection


nums3 = [2, 2, 3, 4, 5, 7, 8]
nums4 = [1, 2, 2, 3, 4, 5, 7]
print(intersection_of_arrays(nums3, nums4))
