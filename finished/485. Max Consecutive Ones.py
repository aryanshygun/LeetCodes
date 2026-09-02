from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        count = 0
        for i in nums:
            if i == 1:
                x += 1
                count = max(count, x)
            else:
                x = 0
        return count
