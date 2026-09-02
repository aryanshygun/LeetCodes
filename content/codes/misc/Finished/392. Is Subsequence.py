# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        xdict = {}
        if s in t:
            return True
        if len(s) > len(t):
            return False
        
        for i in range(len(s)):
            if s.count(s[i]) > t.count(s[i]) or s[i] not in t:
                return False
            else:
                xdict[s[i]] = t.index(s[i])
            if list(xdict.values()) != sorted(xdict.values()):
                return False
        return True
    
    
s = 'ab'
t = 'baab'   
e = Solution()
print(e.isSubsequence(s, t))