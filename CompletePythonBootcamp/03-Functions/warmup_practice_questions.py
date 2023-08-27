'''
warmup practice questions
'''

def lesser_of_two_evens(var_a, var_b):
    '''
    function for lesser of 2 evens
    '''
    if var_a%2 == 0 and var_b%2 == 0:
        if var_a >= var_b:
            return var_b
        return var_a
    if var_a >= var_b:
        return var_a
    return var_b


result_0 = lesser_of_two_evens(2,5)
print(result_0)

def animal_crackers(text):
    '''
    function of 2 words withn same starting letter in a string
    '''
    text_list = text.split()
    if text_list[0][0].upper() == text_list[1][0].upper():
        return True
    return False

result_1 = animal_crackers('Randy randy')
print(result_1)


def makes_twenty(n1,n2):
    '''
    Makes twenty
    '''
    if n1 == 20 or n2 == 20 or n1+n2 == 20:
        return True
    return False

result_3 = makes_twenty(20,7)
print(result_3)
