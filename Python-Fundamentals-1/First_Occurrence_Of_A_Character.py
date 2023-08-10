def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    x = s.find(to_find)
    return x


s1 = "interview"
to_find1 = "e"

print(find_first_occurrence(s1, to_find1))
