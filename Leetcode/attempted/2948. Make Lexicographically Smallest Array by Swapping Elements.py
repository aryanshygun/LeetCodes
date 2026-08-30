from typing import list


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                x = nums[i]
                y = nums[j]
                if x > y and abs(x - y) <= limit:
                    placeholder = y
                    nums[j] = x
                    nums[i] = placeholder
                    j = i + 1
                else:
                    j += 1
                    continue
        return nums
