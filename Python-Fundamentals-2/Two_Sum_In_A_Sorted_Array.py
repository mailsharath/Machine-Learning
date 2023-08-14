def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """

    dict1 = {}
    for i in range(len(numbers)):
        dict1[numbers[i]] = i
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in dict1 and dict1[complement] != i:
            return [i, dict1[complement]]
    return [-1, -1]