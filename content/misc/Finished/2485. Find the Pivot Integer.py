# https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-04-03

class Solution:
    def pivotInteger(self, n: int) -> int:
        if n < 2:
            return n
        total = (n * (n+1))//2
        for i in range(n):
            summ = (i * (i + 1)) // 2
            if total + i == 2 * summ:
                return i
        return -1