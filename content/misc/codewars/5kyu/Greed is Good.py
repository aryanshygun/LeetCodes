# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    xdict = {}
    for i in dice:
        xdict[i] = xdict.get(i,0) + 1

    x = 0
    for i,j in xdict.items():
        
        if i == 1:
            x += (j // 3)*1000
            x += (j % 3)* 100
            
        elif i == 2:
            x += (j // 3)*200
            
        elif i == 3:
            x += (j // 3)*300
            
        elif i == 4:
            x += (j // 3)*400
            
        elif i == 5:
            x += (j // 3)*500
            x += (j % 3)*50
            
        elif i == 6:
            x += (j // 3)*600
            
    return x

print(score( [5, 1, 3, 4, 1] ))