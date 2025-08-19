# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    i = 0
    while i < len(a):   
        if a[i] in b:
            a.pop(i)
            continue
        i += 1
    return a



