# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1216321643/

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        xdict = {}
        for i in nums:
            xdict[i] = xdict.get(i, 0) + 1
        ydict = {} 
        x = 0
        s = sorted(xdict)
        for i in s:
            ydict[i] = x
            x += xdict[i]
        return [ydict[i] for i in nums]

        
x = Solution()
print(x.smallerNumbersThanCurrent([8,1,2,2,3]))



