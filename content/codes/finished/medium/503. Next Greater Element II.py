from ast import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [-1] * n
        stack = []

        i = 0
        while i < 2 * n:
            idx = i % n

            while stack and nums[idx] > nums[stack[-1]]:
                output[stack.pop()] = nums[idx]

            if i < n:
                stack.append(idx)

            i += 1

        return output