# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    xdict = {}
    for i in text.lower():
        xdict[i] = xdict.get(i, 0) + 1
    x = 0
    for i in xdict.keys():
        if xdict[i] >= 2:
            x += 1
    return x