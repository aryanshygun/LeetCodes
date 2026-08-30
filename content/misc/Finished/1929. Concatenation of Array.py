# https://leetcode.com/problems/concatenation-of-array/submissions/1225167893/

class Solution:
    def getConcatenation(self, nums):
        s = nums[:]
        s.extend(nums)
        return s