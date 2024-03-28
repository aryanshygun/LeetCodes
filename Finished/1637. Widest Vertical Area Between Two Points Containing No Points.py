# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        xlist = sorted(point[0] for point in points)
        xmax = 0
        prev = xlist[0]
        for x in xlist[1:]:
            xmax = max(xmax, x - prev)
            prev = x
        return xmax
