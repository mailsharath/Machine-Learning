def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum1(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        dict1[nums[i]] = i
        complement = target - nums[i]
        if complement in dict1 and dict1[complement] != i:
            return [i, dict1[complement]]
    return [-1, -1]


nums1 = [1, 1, 9, 8, 4]
print(two_sum(nums1, 2))
