# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    x = 'aeiou'
    return sum(1 for i in sentence if i in x)