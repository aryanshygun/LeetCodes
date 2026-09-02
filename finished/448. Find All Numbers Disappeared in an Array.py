from ast import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ints = set(nums)
        whole = {i for i in range(1, len(nums) + 1)}
        return list(whole - ints)
