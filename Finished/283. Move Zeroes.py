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
            if [l] != 0:
                l = r
                r += 1
            elif [r] == 0:
                r += 1
            elif [r] != 0:
                [l], [r] = [r], [l]
                l += 1
                r += 1
        return 
    
    
    
        
x = Solution()
nums = [1,2,2,1,1,0]
nums = [1,2,2,1,1,0]
nums = [1,2,2,1,1,0]
nums = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

print(x.moveZeroes(nums))