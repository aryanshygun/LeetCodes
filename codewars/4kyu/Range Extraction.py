# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/solutions/python?filter=me&sort=best_practice&invalids=false

def solution(args):
    # your code here
    x = []
    l = 0
    r = 1
    while r < len(args):
        if args[r] - args[l] != 1:
            x.append(args[l])
            l += 1
            r += 1
        else:
            tmp = []
            while r < len(args) and args[r] - args[l] == 1:
                tmp.append(args[l])
                l += 1
                r += 1
            # else:
            tmp.append(args[l])
            if len(tmp) >= 3:
                x.append(f'{tmp[0]}-{tmp[-1]}')
            else:
                x.extend(tmp)

            l += 1
            r += 1
    if abs(args[-1] - args[-2]) != 1:
        x.append(args[-1])
    return ','.join(str(i) for i in x)