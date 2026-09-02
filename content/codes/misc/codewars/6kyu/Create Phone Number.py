# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

def create_phone_number(n):
    x = ''.join(str(i) for i in n[0:3])
    y = ''.join(str(i) for i in n[3:6])
    z = ''.join(str(i) for i in n[6:])
    return f'({x}) {y}-{z}'