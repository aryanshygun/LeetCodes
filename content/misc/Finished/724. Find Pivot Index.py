# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def pivotIndex(self, nums) -> int:
        total = sum(nums)
        i = 0
        while i < len(nums):
            leftsum = sum(nums[:i])
            if leftsum == total - leftsum - nums[i]:
                return i
            i += 1
        return -1
        
        
        
        
        
        
        
        
n = Solution()
x = [1,7,3,6,5,6]
# x = [1,2,3]
print(n.pivotIndex(x))