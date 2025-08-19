# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python

def last_digit(n1, n2):
    num1 = n1 % 100
    num2 = n2 % 100
    if n2 == 0:
        return 1
    if n1 % 10 == 0:
        return 0
    
    memo = {}
    for i in range(2, 100):
        sub = {}
        for j in range(1, 100):
            x = pow(i,j) % 10
            # if x not in sub.values():
            sub[(i,j)] = x
        memo[i] = sub
    
    return memo[num1][(num1, num2)]
