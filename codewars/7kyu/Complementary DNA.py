# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

def DNA_strand(dna):
    xlist = [*dna]
    for i in range(len(xlist)):
        if xlist[i] == 'A':
            xlist[i] = 'T'
        elif xlist[i] == 'T':
            xlist[i] = 'A'
        elif xlist[i] == 'C':
            xlist[i] = 'G'
        elif xlist[i] == 'G':
            xlist[i] = 'C'
    return xlist