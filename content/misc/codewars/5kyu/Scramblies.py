# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

def scramble(str1,str2):
    xdict = {}
    ydict = {}
    for i in str1:
        xdict[i] = xdict.get(i, 0) + 1
    for i in str2:
        ydict[i] = ydict.get(i, 0) + 1
    
    for i, j in ydict.items():
        if i not in xdict or xdict[i] < j:
            return False
    return True
        
        
        
        
        
    return True


print(scramble("rkqodlw", "world"))