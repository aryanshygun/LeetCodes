# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    xlist = [*sequence]
    if len(xlist) == 1:
        return xlist
    l = 0
    r = 1
    while r < len(xlist):
        if xlist[r] == xlist[l]:
            xlist.pop(r)
        else:
            l += 1
            r += 1
    return xlist




x = 'AAAABBBCCDAABBB'
print(unique_in_order(x))