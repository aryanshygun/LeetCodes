# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

def sum_for_list(lst):
    primelist = []

    for i in lst:
        for j in range(2, int(abs(i)**0.5) + 1):
            while abs(i) % j == 0:
                primelist.append(j)
                i //= j
        if abs(i) > 1:
            primelist.append(abs(i))
    primelist = list(set(primelist))
    ans = []
    for i in primelist:
        x = 0
        for j in lst:
            if j % i == 0:
                x += j
        ans.append([i, x])
    ans.sort(key = lambda x:x[0])
    return ans
