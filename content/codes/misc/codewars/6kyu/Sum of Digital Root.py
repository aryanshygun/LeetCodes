# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    if n < 10:
        return n
    n = sum(int(i) for i in str(n))
    # n // = 10
    return digital_root(n)
    
