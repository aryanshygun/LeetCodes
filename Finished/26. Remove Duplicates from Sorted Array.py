# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):     
        i = 0
        while i < len(nums) - 1 and nums[i+1] != '_':
            a, b = nums[i], nums[i+1]
            if a < b:
                i += 1
                continue
            nums.pop(i+1)
            nums.append('_')
        return len(set(nums[:i+1]))
        