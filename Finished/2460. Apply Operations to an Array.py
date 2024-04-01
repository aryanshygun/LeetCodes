# https://leetcode.com/problems/apply-operations-to-an-array/submissions/1219968824/

class Solution:
    def applyOperations(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            else:
                pass
        l, r = 0, 1
        while r < len(nums):
            if nums[l] != 0:
                l = r
                r += 1
            elif nums[r] == 0:
                r += 1
            elif nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
        return nums
    
    
    
    
        
x = Solution()
nums = [1,2,2,1,1,0]

print(x.applyOperations(nums))