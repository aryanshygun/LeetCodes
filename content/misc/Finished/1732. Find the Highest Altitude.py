# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def largestAltitude(self, gain) -> int:
        ylist = [0]
        l = 0
        while l < len(gain):
            y = ylist[-1]
            ylist.append(y + gain[l])
            l += 1
        return max(ylist)