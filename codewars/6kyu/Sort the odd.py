# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):
    odds = [i for i in source_array if i % 2 != 0]
    odds.sort()
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds.pop(0)
    return sour




print(sort_array([5, 8, 6, 3, 4]))