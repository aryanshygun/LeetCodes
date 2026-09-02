from typing import list


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            nums[i] = None
            if x in nums:
                return [i, nums.index(x)]
