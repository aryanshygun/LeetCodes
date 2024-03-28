# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

class Solution:
    def minOperations(self, nums, k):
        return sum(1 for i in sorted(nums) if i < k)