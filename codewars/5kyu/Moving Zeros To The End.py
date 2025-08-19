# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(lst):
    l = 0
    r = 1
    while r < len(lst):
        if lst[l] != 0:
            l = r
            r += 1
        elif lst[r] == 0:
            r += 1
        elif lst[r] != 0:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r += 1
    return lst
