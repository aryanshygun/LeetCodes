# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        else:
            reversed_x = 0
            while x > 0:
                digit = x % 10
                reversed_x = reversed_x * 10 + digit
                x //= 10
        return x == reversed_x
    
a = Solution()
print(a.isPalindrome(121))