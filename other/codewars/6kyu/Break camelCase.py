# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
    l = 0
    xlist = [*s]
    while l < len(xlist):
        a = xlist[l]
        if a == a.lower():
            l +=1
        else:
            xlist.insert(l, ' ')
            l += 2
            
    return ''.join(xlist)

    
print(solution('camelCasingBreak'))