# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    l = 0
    while l < len(arr):
        if sum(arr[:l]) == sum(arr[l+1:]):
            return l
        else:
            l += 1
    return -1




print(find_even_index([1,2,3,4,3,2,1]))

