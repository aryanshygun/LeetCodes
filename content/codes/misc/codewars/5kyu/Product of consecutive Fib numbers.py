# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

def product_fib(_prod):
    fibs = {0:0, 1:1}
    def fib(n):
        if n in fibs:
            return fibs[n]
        fibs[n] = fib(n - 1) + fib(n - 2)
        return fibs[n]
    n = 0
    while fib(n) * fib(n+1) < _prod:
        n += 1   
    return [fib(n), fib(n+1), fib(n) * fib(n+1) == _prod]

