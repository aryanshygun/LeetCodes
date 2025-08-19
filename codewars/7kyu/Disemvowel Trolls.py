# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    x = 'aeiouAEIOU'
    y = ''
    for i in string_:
        if i not in x:
            y += i
    return y