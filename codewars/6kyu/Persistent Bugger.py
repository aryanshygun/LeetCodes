# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    x = str(n)
    times = 0
    while len(x) > 1:
        y = 1
        times += 1
        for i in x:
            y *= int(i)
        x = str(y)
    return times
    
    
    