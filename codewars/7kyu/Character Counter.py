# https://www.codewars.com/kata/56786a687e9a88d1cf00005d/solutions/python

def validate_word(word):
    xdict = {}
    for i in word.lower():
        xdict[i] = xdict.get(i, 0) + 1
    return len(set(xdict.values())) == 1
    