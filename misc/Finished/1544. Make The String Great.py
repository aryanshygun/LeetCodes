# https://leetcode.com/problems/make-the-string-great/submissions/1224000231/?envType=daily-question&envId=2024-04-05

class Solution:
    def makeGood(self, s: str) -> str:
        xlist = [*s]
        l = 0
        while l < len(xlist) - 1:
            x = xlist[l]
            y = xlist[l+1]
            if x.lower() == y.lower() and x != y:
                xlist.pop(l)
                xlist.pop(l)
                l = 0
            else:
                l +=1    
        return ''.join(xlist)