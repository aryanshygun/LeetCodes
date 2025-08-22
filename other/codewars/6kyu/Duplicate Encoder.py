# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

def duplicate_encode(word):
    xdict = {}
    for i in word.lower():
        xdict[i] = xdict.get(i, 0) + 1
    x = ''
    for i in word:
        if xdict[i] > 1:
            x += ')'
        else:
            x += '('
    return x