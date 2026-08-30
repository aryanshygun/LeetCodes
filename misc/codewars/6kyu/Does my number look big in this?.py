# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

def narcissistic( value ):
    x = str(value)
    y = 0
    for i in x:
        y += int(i)**len(x)
    return y == value