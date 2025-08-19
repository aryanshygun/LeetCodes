# https://www.codewars.com/kata/536a155256eb459b8700077e/solutions/python?filter=me&sort=best_practice&invalids=false

def create_spiral(n):
    if type(n) != int:
        return []
    if n < 1:
        return []
    xlist = [[0]*n for i in range(n)]

    num = 1
    top, left = 0, 0
    bot, right = n - 1, n - 1



    while num <= n*n:
        for i in range(left, right + 1):
            xlist[top][i] = num
            num += 1
        top += 1
        for i in range(top, bot + 1):
            xlist[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left -1 , -1 ):
            xlist[bot][i] = num
            num += 1
        bot -= 1
        for i in range(bot, top - 1, -1):
            xlist[i][left] = num
            num += 1
        left += 1
    return xlist