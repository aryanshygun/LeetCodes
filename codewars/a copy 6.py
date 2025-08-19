def comp(array1, array2):
    
    if array1 is None or array2 is None:
        return False

    xdict = {}
    for i in array1:
        xdict[i] = xdict.get(i, 0) + 1
        
    ydict = {}
    for i in array2:
        x = i**(1/2)
        ydict[x] = ydict.get(x, 0) + 1

    return xdict == ydict





a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1, a2))

