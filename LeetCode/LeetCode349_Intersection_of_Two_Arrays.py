def intersection_of_arrays(numbers1, numbers2):
    intersection = []
    l1 = len(numbers1)
    l2 = len(numbers2)
    if l1 > l2:
        for item in numbers2:
            if item in numbers1:
                if item not in intersection:
                    intersection.append(item)

    else:
        for item in numbers1:
            if item in numbers2:
                if item not in intersection:
                    intersection.append(item)

    if len(intersection) > 0:
        return intersection

    return [-1]


nums3 = [2, 2, 3, 4, 5, 7, 8]
nums4 = [1, 2, 2, 3, 4, 5, 7]
print(intersection_of_arrays(nums3, nums4))
