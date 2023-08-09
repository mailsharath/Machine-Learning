def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    s1 = s.strip()
    s2 = s.split()
    s2.reverse()
    return ' '.join(s2)


s = "courses prep interview technical best"

print(reverse_words(s))
