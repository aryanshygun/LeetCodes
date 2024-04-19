# https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1236119824/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t = ''

        def check(x, y):
            if len(x) % len(y) != 0 or y not in x:
                return False
            
            ylist = [x[i:i+len(y)] for i in range(0, len(x), len(y))]
            return all(sub == y for sub in ylist)
            
            
        for i in range(len(str1)):
            for j in range(i, len(str1)):
                a = str1[i:j+1]
                if check(str2, a) and check(str1, a):
                    if len(a) > len(t):
                        t = a
                    else:
                        t = t
        return t



'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def dividble(s, sub):
            if not s:
                return False
            n = len(s) // len(sub)
            return sub * n == s
        xwordx = gcd(len(str1), len(str2))
        xword = str1[:xwordx]

        if dividble(str1, xword) and dividble(str2, xword):
            return xword
        else:
            return ''
            '''