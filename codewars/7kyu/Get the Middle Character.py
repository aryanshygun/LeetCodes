# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

def get_middle(s):
    if len(s) % 2 == 0:
        return s[(len(s) // 2) - 1:(len(s) // 2) + 1]
    else:
        return s[(len(s) // 2)]