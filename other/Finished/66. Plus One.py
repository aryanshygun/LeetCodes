# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        x = -1
        while abs(x) <= len(digits) and digits[x] == 9:
            digits[x] = 0
            x -= 1
        else:
            try:
                digits[x] += 1
            except IndexError:
                digits.insert(0, 1)
        return digits