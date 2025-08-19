# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
    num = str(n)
    x = 0
    for i in num:
        x += int(i)**p
        p += 1
    if x % n == 0:
        return int(x / n)
    return -1
    
print(dig_pow(89, 1))