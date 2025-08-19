# https://www.codewars.com/kata/52945ce49bb38560fe0001d9/train/python

def pascal(p):
    n = p
    i = 1
    xlist = []
    while i <= n:
        tmp = []
        for j in range(1, 1 + i):
            if j == 1 or j == i or i == 1:
                x = 1
            else: 
                x = xlist[i-2][j-1] + xlist[i-2][j-2]
            tmp.append(x)
        xlist.append(tmp)
        i += 1
    x = len(xlist) + 3
    i = 0
    show = []
    while i < len(xlist):
        a = ' '*x
        b = '   '.join(str(i) for i in xlist[i])
        i += 1
        x -= 2    
        show.append(a + b)
        # print(a + b)

    return xlist


