# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/1225097877/?envType=daily-question&envId=2024-04-06

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        x = 0
        arr = [*s]

        for i in range(len(arr)):
            if arr[i] == '(':
                x += 1
            elif arr[i] == ')':
                if x == 0:
                    arr[i] = '*' 
                else:
                    x -= 1

        for i in range(len(arr) - 1, -1, -1):
            if x > 0 and arr[i] == '(':
                arr[i] = '*'
                x -= 1
        
        return ''.join(c for c in arr if c != '*')
    
     