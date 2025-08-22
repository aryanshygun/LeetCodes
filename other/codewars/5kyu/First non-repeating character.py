# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(s):
    xdict = {}
    for i in s.lower():
        xdict[i] = xdict.get(i, 0) + 1
    for i in s:
        if xdict[i.lower()] == 1:
            return i
    return ''
