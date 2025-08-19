# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

def strip_comments(strng, markers):
    str = strng.split('\n')
    a = ''
    i = 0
    tmp = []
    while i < len(str):
        line = str[i]
        ii = 0
        x = ''
        while ii < len(line):
            letter = line[ii]
            yes = any(a in letter for a in markers)
            if yes:
                break
            else:
                x += letter
                ii += 1
        tmp.append(x)
        i += 1
    for i,j in enumerate(tmp):
        if j == '\t':
            tmp[i] = '' 
    a += '\n'.join(i.rstrip(' ') for i in tmp)

        
    return a
