# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python

def tribonacci(signature, n):
    xlist = signature
    if n < 4:
        return signature[:n]
    for i in range(4, n + 1):
        x = sum(j for j in xlist[-1:-4:-1])
        xlist.append(x)
    return xlist
    
    
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)


print(tribonacci([1, 2, 3], 4))