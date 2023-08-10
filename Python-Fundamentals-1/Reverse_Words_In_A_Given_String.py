def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    s1 = s.strip()
    s2 = s1.split()
    s2.reverse()
    return ' '.join(s2)


sen = "courses prep interview technical best"

print(reverse_words(sen))
