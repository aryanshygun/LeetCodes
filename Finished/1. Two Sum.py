# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1::]:
                return [i, nums[i + 1::].index(target - nums[i]) + i + 1]
        