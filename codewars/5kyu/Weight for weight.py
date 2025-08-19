# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

def order_weight(strng):
    xlist = []
    for i in strng.split():
        x = sum(int(j) for j in i)
        xlist.append((i, x))
    sortt = sorted(xlist, key=lambda x:(x[1], x[0]))
    return ' '.join(i[0] for i in sortt)



