class Solution:
    def twoSum(self, nums: List[int], target):
        idx = 0
        view = {}
        while idx < len(nums):
            diff = target - nums[idx]
            if diff in view:
                return [view[diff],idx]
            else:
                view[nums[idx]] = idx
            idx += 1
nums = [2,7,11,15]
target = 9
              
a = Solution()
print(a.twoSum(nums, target))