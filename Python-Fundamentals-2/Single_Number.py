def single_number(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    dict1 = {}
    for i in range(len(arr)):
        if arr[i] in dict1.keys():
            dict1[arr[i]] +=1
        else:
            dict1[arr[i]] = 1
    for j, k in dict1.items():
        if k == 1:
            return j
    return 0
