from ast import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        xdict = {}
        stack = []
        i = 0
        while i < len(nums2):
            while stack and nums2[i] > stack[-1]:
                idx = stack.pop()
                xdict[idx] = nums2[i]
            stack.append(nums2[i])
            i += 1

        while stack:
            xdict[stack[-1]] = -1
            stack.pop()

        return [xdict.get(num, 0) for num in nums1]
