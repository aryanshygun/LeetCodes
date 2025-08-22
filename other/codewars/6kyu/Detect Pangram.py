# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(x):
    xlist = [chr(i) for i in range(97,123)]
    for i in xlist:
        if i not in x.lower():
            return False
    return True
x = "The quick brown fox jumps over the lazy dog"

print(is_pangram(x))

