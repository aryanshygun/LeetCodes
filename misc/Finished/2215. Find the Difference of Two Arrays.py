# https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1219579931/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        ans1 = []
        ans2 = []

        for i in set1:
            if i not in set2:
                ans1.append(i)
        for i in set2:
            if i not in set1:
                ans2.append(i)
                
        return [ans1, ans2]



x = Solution()
a = [1,2,3,3]
b = [1,1,2,2]


print(x.findDifference(a, b))