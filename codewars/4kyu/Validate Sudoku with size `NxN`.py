# https://www.codewars.com/kata/540afbe2dc9f615d5e000425/train/python

class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        xlist = self.data
        
        for i in xlist:
            for j in i:
                if isinstance(j, int) == False or j is True:
                    return False

        # test if its a perfect square
        rows = len(xlist)
        for i in xlist:
            if len(i) != rows:
                return False
        # test if rows got correct nums
        numlist = [y for y in range(1, len(i)+1)]
        for i in xlist:
            for j in i:
                if j not in numlist:

                    return False
        # test if columns got correct nums  
        for i in xlist:
            if i[0] not in numlist:
                return False
        # test if smol squares got correct nums
        a = int(len(xlist) ** (1/2))
        for i in range(0,rows, a):
            for j in range(0,rows, a):
                square = [xlist[w][q] for w in range(i,i+a) for q in range(j, j+ a)]
                if len(set(square)) != len(numlist):
                    return False
        return True