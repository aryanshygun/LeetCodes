# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    xlist = sentence.split()
    for i in range(len(xlist)):
        if len(xlist[i]) >= 5:
            xlist[i] = xlist[i][::-1]
    return ' '.join(xlist)