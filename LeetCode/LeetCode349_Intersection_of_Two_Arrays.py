def intersection_of_arrays(nums1, nums2):
    intersection = []
    l1 = len(nums1)
    l2 = len(nums2)
    if l1 > l2:
        for item in nums2:
            if item in nums1:
                if item not in intersection:
                    intersection.append(item)
        return intersection

    else:
        for item in nums1:
            if item in nums2:
                if item not in intersection:
                    intersection.append(item)
        return intersection


nums3 = [2, 2, 3, 4, 5, 7, 8]
nums4 = [1, 2, 2, 3, 4, 5, 7]
print(intersection_of_arrays(nums3, nums4))
