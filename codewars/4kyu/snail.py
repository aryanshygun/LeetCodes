# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/solutions/python?filter=me&sort=best_practice&invalids=false

def snail(snail_map):
    ylist = []

    while snail_map:

        ylist.extend(snail_map.pop(0))

        for i in snail_map:
            if i:
                ylist.append(i.pop())


        if snail_map:
            ylist.extend(snail_map.pop()[::-1])

        for i in reversed(snail_map):
            if i:
                ylist.append(i.pop(0))
    return ylist