def generate_sorted_array_of_squares(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    numbers_squared = []
    for i in numbers:
        numbers_squared.append(i*i)
    numbers_squared.sort()

    return numbers_squared
