# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(message):
    upperlist = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    lowerlist = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    l = 0
    x = ''
    while l < len(message):
        if message[l] in upperlist:
            x += upperlist[(upperlist.index(message[l]) + 13) % len(upperlist)]
        elif message[l] in lowerlist:
            x += lowerlist[(lowerlist.index(message[l]) + 13) % len(lowerlist)]
        else:
            x += message[l]
        l += 1
    return x
