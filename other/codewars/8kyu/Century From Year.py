# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

def century(year):
    century = year // 100
    if century*100 == year:
        return century
    else:
        return century + 1