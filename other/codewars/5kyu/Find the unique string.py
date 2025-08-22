      
def find_uniq(arr):
    xlist = []
    for i in range(len(arr)):
        x = arr[i].replace(' ', '').lower()
        xlist.append(''.join(set(x)))
    # return xlist
    l = 2
    if xlist[0] == xlist[1]:
        while l < len(arr) and xlist[l] == xlist[0]:
            l += 1
        else:
            return arr[l]
    else:
        if xlist[2] == xlist[0]:
            return arr[1]
        elif xlist[2] == xlist[1]:
            return arr[0]
    return None








print(find_uniq([ 'Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter' ]))
print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))
