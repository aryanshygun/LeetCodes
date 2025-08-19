# https://www.codewars.com/kata/5d376cdc9bcee7001fcb84c0/train/python

def odd_ones_out(numbers):
    xlist = []
    for i in numbers:
        if numbers.count(i) % 2 ==0:
            xlist.append(i)
    return xlist