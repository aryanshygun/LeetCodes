# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

def is_square(n):    
    if n < 0:
        return False
    x = n**(1/2)
    if x % 1 == 0:
        return True
    return False