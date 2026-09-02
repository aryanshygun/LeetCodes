# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def increasingTriplet(self, nums) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num 
            else:
                return True 
        return False
    
    
nums = [2,1,5,0,4,6]
nums = [20,100,10,12,5,13]
nums = [1,5,0,4,1,3]

x = Solution()
print(x.increasingTriplet(nums))



