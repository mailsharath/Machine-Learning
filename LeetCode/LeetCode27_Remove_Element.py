def remove_element(nums, number):
    nums[:] = [num for num in nums if num != number]
    return len(nums)


nums1 = [1, 2, 3, 4, 5, 6]
number1 = 6
print(remove_element(nums1, number1))
print(nums1)
