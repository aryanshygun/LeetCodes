# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    xdict = {'x':0, 'o':0}
    for i in s:
        if i.lower() == 'x':
            xdict['x'] += 1
        elif i.lower() == 'o':
            xdict['o'] += 1
            
    if xdict['x'] == xdict['o']:
        return True
    return False