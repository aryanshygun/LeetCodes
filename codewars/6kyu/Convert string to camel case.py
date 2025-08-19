# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

import re
def to_camel_case(text):
    result = re.split(r'[_-]', text)
    xlist = [*text]
    for i in range(1, len(result)):
        result[i] = result[i].title()
    return ''.join(result)