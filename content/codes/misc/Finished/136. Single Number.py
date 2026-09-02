# https://leetcode.com/problems/single-number/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def singleNumber(self, nums):
        xdict = {}
        for i in nums:
            xdict[i] = xdict.get(i, 0) + 1
        for i, j in xdict.items():
            if j == 1:
                return i
nums = [2,2,1]
x = Solution()
print(x.singleNumber(nums))