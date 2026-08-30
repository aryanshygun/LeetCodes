# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val: int) -> int:
        x = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                x += 1
            else:
                i += 1
