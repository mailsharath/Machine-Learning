def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    i = 0
    for k in s:
        if k.isalpha():
            i += 1
    return i


s1 = "#aBdj12C"

print(count_alphabets(s1))
