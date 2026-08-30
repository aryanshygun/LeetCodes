class Solution:
    def maxDistinct(self, s: str) -> int:
        i = 0
        xlist = []
        for i in s:
            if i not in xlist:
                xlist.append(i)
        return len(xlist)


class Solution2:
    def maxDistinct(self, s: str) -> int:

        return len(set(s))
