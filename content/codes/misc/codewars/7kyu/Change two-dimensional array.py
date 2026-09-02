# https://www.codewars.com/kata/581214d54624a8232100005f/train/python

def matrix(array): 
    for i in range(len(array)):
        if array[i][i] >= 0:
            array[i][i] = 1
        else:
            array[i][i] = 0  
    return array
