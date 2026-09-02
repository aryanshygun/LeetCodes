from ast import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * 2 * len(nums)
        for i in range(len(nums)):
            output[i] = nums[i]
            output[i + len(nums)] = nums[i]
        return output
