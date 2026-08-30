# https://leetcode.com/problems/number-of-good-pairs/submissions/1216212282/

class Solution:
    
    def numIdenticalPairs(self, nums) -> int:
        
        xnum = 0
        for i in set(nums):
            if nums.count(i) > 1:
                x = nums.count(i)
                xnum += (x*(x-1))/2
        return int(xnum)
    
    
    
y = Solution()

print(y.numIdenticalPairs([1,2,3,1,1,3]))
    
    
    

