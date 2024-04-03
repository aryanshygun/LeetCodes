# https://leetcode.com/problems/pascals-triangle/description/


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 1
        xlist = []
        n = numRows
        while i <= n:
            tmp = []
            for j in range(1, 1 + i):
                if j == 1 or j == i or i == 1:
                    x = 1
                else: 
                    x = xlist[i-2][j-1] + xlist[i-2][j-2]
                tmp.append(x)
            xlist.append(tmp)
            i += 1
        return xlist
