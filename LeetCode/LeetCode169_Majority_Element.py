def majority_element(nums):
    dict1 = {}
    for i in range(len(nums)):
        if nums[i] in dict1.keys():
            dict1[nums[i]] += 1
        else:
            dict1[nums[i]] = 1
    for j, k in dict1.items():
        if k > len(nums)/2:
            return j


nums1 = [3, 3, 3, 2, 2, 2, 3]
print(majority_element(nums1))



