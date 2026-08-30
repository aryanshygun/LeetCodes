# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
    xdict = {'odd':0,'even':0}
    for i in integers:
        if xdict['even'] > 1 or xdict['odd'] > 1:
            break
        if i % 2 == 0:
            xdict['even'] += 1
        else:
            xdict['odd'] += 1
    if xdict['even'] > 1:
        for i in integers:
            if i % 2 != 0:
                return i
    elif xdict['odd'] > 1:
        for i in integers:
            if i % 2 == 0:
                return i
print(find_outlier([1,1,-1,1,1,-44,7,7,7,7,7,7,7,7]))

'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
'''