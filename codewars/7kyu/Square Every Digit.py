# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

def square_digits(num):
    xlist = [*str(num)]
    ylist = []
    for i in xlist:
        x = int(i) ** 2
        ylist.append(str(x))
    return int(''.join(ylist))
        