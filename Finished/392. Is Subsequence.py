# s = "acb"
# s = 'abc'
# t = "ahbgdc"
s = 'ab'
t = 'baab'
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        xdict = {}
        for i in range(len(s)):
            if s.count(s[i]) > t.count(s[i]):
                return False
            if s[i] not in t:
                return False
            else:
                xdict[s[i]] = t.index(s[i])

            if list(xdict.values()) != sorted(xdict.values()):
                return False
        return True
    
    
e = Solution()
print(e.isSubsequence(s, t))