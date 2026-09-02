from ast import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = [0] * 2
        counts = {}

        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
            if counts[nums[i]] == 2:
                output[0] = nums[i]
            if i + 1 not in nums:
                output[1] = i + 1
        return output
