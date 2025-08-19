# https://www.codewars.com/kata/520b9d2ad5c005041100000f/solutions/python

def pig_it(text):
    y = []
    for i in text.split():
        if i.isalpha():
            i += i[0] + 'ay'
            i = i[1:]
        y.append(i)
    return ' '.join(y)