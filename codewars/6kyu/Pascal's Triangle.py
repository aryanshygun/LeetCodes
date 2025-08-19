# https://www.codewars.com/kata/5226eb40316b56c8d500030f/solutions/python?filter=me&sort=best_practice&invalids=false

def pascals_triangle(n):
    pass
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
    ylist = []
    for i in xlist:
        for j in i:
            ylist.append(j)
    return ylist