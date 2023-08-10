def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    """
    res = []
    for i in a:
        if i in b:
            res.append(i)
            b.remove(i)
    return res


a1 = [4, 2, 2, 3, 1]
b1 = [2, 2, 2, 3, 3]

print(get_intersection_with_maintained_frequency(a1, b1))
