# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string(strng):
    if strng.isalpha():
        return strng + '1'
    if strng == '':
        return '1'
    if strng.isdigit():
        return str(int(strng) + 1).zfill(len(strng))
    i = len(strng)
    while strng[i - 1].isdigit() == True:
        i -= 1
    a = strng[:i]
    b = strng[i:]
    return a + str(int(b) + 1).zfill(len(b))








print(increment_string("0076"))