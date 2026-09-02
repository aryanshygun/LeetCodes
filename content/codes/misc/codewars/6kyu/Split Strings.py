# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
    xlist = []
    for i in range(0, len(s), 2):
        x = s[i:i+2]
        if len(x) == 1:
            x += '_'
        xlist.append(x) 
    return xlist

print(solution("asdfads"))