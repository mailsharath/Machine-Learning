def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    # Write your code here.
    word_list = sentence.split()
    if len(word_list) == 0:
        return 0
    return len(word_list[-1])


str1 = 'what is the length of crocodile'

print(length_of_last_word(str1))
