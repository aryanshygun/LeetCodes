# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 1
        while r < len(nums):
            # if nums[l] == 0:
                
            # else:
            #     l += 1
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

print(x.moveZeroes(nums))