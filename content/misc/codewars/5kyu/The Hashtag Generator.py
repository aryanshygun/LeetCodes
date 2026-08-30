# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    if s == '':
        return False
    
    word = '#' + ''.join(list(map(str.title, s.split())))
    return False if len(word) > 140 else word