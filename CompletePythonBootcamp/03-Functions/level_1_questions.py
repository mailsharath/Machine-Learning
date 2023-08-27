'''
Level 1 Questions
'''

def old_macdonald(name):
    '''
    Capitalize 1st and 4th Characters
    '''
    new_name = name.capitalize()
    name_list = list(new_name)
    name_list[3] = name_list[3].upper()
    final_name = ''.join(name_list)
    return final_name


result_name = old_macdonald('macdonald')
print(result_name)

def master_yoda(text):
    '''
    Master Yoda Text Conversion
    '''
    name_text = text.split()
    
    yoda_text = ' '.join(name_text[::-1])
    return yoda_text

yoda_result = master_yoda('My name is Sharath')
print(yoda_result)


def almost_there(n):
    '''
    Almost there 100 or 200
    '''
    if (n >= 90 and n <= 110) or (n >= 190 and n <=210):
        return True
    return False


result = almost_there(92)
print(result)