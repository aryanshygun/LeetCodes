# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    xdict = {}
    for i in seq:
        xdict[i] = xdict.get(i, 0) + 1
    for i, j in xdict.items():
        if j % 2 != 0:
            return i