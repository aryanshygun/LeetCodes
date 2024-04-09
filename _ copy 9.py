def makeGood(s: str) -> str:
    if len(str) == 1:
        return str
    xlist = [*s]
    l = 0
    while l < len(xlist) - 1:
        x = xlist[l]
        y = xlist[l+1]
        if (x.lower() == y or x == y.lower()) and x != y:
            xlist.pop(l)
            xlist.pop(l)
            l = 0
        else:
            l +=1    
    return ''.join(xlist)
# s = "leEeetcode"
s = "abBAcC"
print(makeGood(s))