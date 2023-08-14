def find_maximum_sum_subarray(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    max_value = numbers[0]
    for i in range(len(numbers)):
        sum1 = numbers[i]
        if sum1 > max_value:
            max_value = sum1
        for j in range(i + 1, len(numbers)):
            sum1 += numbers[j]
            if sum1 > max_value:
                max_value = sum1
    return max_value
