# https://www.codewars.com/kata/5b93fecd8463745630001d05

def snail(column, day, night):
    diff = day - night
    distance = night
    days = 0
    if diff > column or day > column:
        return 1
    while distance < column:
        distance += diff
        days += 1
    return days