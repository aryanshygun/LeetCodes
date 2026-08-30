class Solution:
    def countValidPrefixes(self, s: str) -> int:
        l = 0
        xlist = {0: 0, 1: 0}
        count = 0
        while l < len(s):
            xlist[int(s[l])] += 1
            if abs(xlist[int(s[l])] - xlist[1 - int(s[l])]) <= 1:
                count += 1
            l += 1
        return count
