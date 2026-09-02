# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python          
            
def find_uniq(arr):
    l = 2
    if arr[0] == arr[1]:
        while l < len(arr) and arr[l] == arr[0]:
            l += 1
        return arr[l]
    if arr[3] == arr[0]:
        return arr[1]
    elif arr[3] == arr[1]:
        return arr[0]
    return None
        