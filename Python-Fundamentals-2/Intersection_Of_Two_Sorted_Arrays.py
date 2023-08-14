def get_intersection(numbers1, numbers2):
    """
    Args:
     numbers1(list_int32)
     numbers2(list_int32)
    Returns:
     list_int32
    """
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