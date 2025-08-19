# https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python

def is_prime(num):
    if num == 0 or num == 1 or num < 0:
        return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True






print(is_prime(4))