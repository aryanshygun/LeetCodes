# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        key = {}
        for i, j in enumerate(nums):
            key[j] = i
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in key and key[tmp] != i:
                return [i, key[tmp]]