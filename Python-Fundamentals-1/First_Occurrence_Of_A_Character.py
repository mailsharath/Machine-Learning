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


s = "interview"
to_find = "e"

print(find_first_occurrence(s, to_find))