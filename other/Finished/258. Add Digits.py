# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            x = str(num)
            y = 0
            for i in x:
                y += int(i)
            num = y
        return num
