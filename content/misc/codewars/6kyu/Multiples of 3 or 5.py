# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    if number < 0:
        return 0
    x = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            x += i
        elif i % 3 == 0 and i % 5 == 0:
            x += i
    return x