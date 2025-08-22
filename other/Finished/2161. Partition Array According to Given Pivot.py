# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums, pivot):
        xlist = []
        alist = []
        ylist = []
        for i in nums:
            if i < pivot:
                xlist.append(i)
            elif i == pivot:
                alist.append(i)
            else:
                ylist.append(i)
        return xlist + alist + ylist
    
a = Solution()
nums = [9,12,5,10,14,3,10]


pivot = 10
print(a.pivotArray(nums, pivot))