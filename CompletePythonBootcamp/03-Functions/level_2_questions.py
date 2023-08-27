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
    if a+b+c <= 21:
        return a+b+c
    elif a+b+c > 21 and (a==11 or b==11 or c==11) and a+b+c-10 <= 21:
        return a+b+c-10
    return 'Bust'


result_total = blackjack(9,9,11)
print(result_total)


def summer_69(arr):
    '''
    Summer of 69
    '''
    sum_check = True
    sum_total = 0
    for item in arr:
        if item != 6 and sum_check:
            sum_total += item
        elif item == 6:
            sum_check = False
        elif item == 9 and not sum_check:
            sum_check = True
    return sum_total

result_sum = summer_69([2, 1, 6, 9, 9, 11])        
print(result_sum)
