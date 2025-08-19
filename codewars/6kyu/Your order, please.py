# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python


def order(sentence):
    ylist = [0]*len(sentence.split())
    for i in sentence.split():
        for j in i:
            if j.isdigit():
                ylist[int(j)-1] = i
    return ' '.join(ylist)


