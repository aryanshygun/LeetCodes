# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/solutions/python?filter=me&sort=best_practice&invalids=false

def solution(text, ending):
    return ending[::-1] == text[-1:-len(ending)-1:-1]