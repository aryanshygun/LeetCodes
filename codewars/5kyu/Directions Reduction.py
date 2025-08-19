# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

def dir_reduc(arr):
    xdict = {'NORTH':'SOUTH',
             'SOUTH':'NORTH',
             'WEST':'EAST',
             'EAST':'WEST'}
    l = 0
    while l < len(arr) - 1:
        if xdict[arr[l]] == arr[l + 1]:
            arr.pop(l)
            arr.pop(l)
            l = 0
        else:
            l += 1
    return arr
