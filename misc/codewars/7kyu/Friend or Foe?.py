# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

def friend(x):
    i = 0
    while i < len(x):
        if len(x[i]) != 4:
            x.pop(i)
        else:
            i += 1
    return x