# https://leetcode.com/problems/missing-number/?envType=daily-question&envId=2024-04-03

class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        return int(n*(n+1)/2 - sum(nums))