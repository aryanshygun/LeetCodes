from typing import list


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            nums[i] = None
            if x in nums:
                return [i, nums.index(x)]
            
            
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        while i <len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1