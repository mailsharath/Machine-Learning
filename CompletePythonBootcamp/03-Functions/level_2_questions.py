'''
Level Two Questions
'''


def has_33(nums):
    '''
    Find 33 in integer list
    '''
    for index in range(len(nums)-1):
        if nums[index] == 3 and nums[index+1] == 3:
            return True
    return False  

result = has_33([3,1,3]) 
print(result)


def paper_doll(text):
    '''
    Paper Doll
    '''
    text_list = list(text)
    new_list = []
    for item in text_list:
        new_list.append(item)
        new_list.append(item)
        new_list.append(item)
    final_text = ''.join(new_list)
    return final_text

result_text = paper_doll('Mississippi')
print(result_text)


def blackjack(a,b,c):
    '''
    Blackjack
    '''
    
