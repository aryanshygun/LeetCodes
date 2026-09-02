class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        odd = 0
        even = 0

        for num in nums1:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        return bool(even == len(nums1) or odd == len(nums1) or even >= 1 and odd >= 1)
