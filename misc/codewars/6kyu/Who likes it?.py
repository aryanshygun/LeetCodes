# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        x = names[0] + ' likes this'
        return x
    elif len(names) == 2:
        x = ' and '.join(names) + ' like this'
        return x
    elif len(names) == 3:
        x = ', '.join(names[:-1]) + ' and ' + names[-1] + ' like this'
        return x
    else:
        x= names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others like this'
        return x