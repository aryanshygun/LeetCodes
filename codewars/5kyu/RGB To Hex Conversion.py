# print(int('148',16))

def rgb(r, g, b):
    col = [r,g,b]
    xlist = []
    
    for i in col:
        if i < 0 :
            xlist.append('00')
        elif i > 255:
            xlist.append('FF')
        else:
            xlist.append(hex(i)[2:].zfill(2).upper())
    return ''.join(xlist)
