# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

def high_and_low(numbers):
    xlist = [int(i) for i in numbers.split()]
    return str(max(xlist)) + ' ' + str(min(xlist))