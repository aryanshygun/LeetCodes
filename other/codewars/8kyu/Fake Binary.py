# https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python

def fake_bin(x):
    y = ''
    for i in x:
        if int(i) < 5:
            y += '0'
        else:
            y += '1'
    return y