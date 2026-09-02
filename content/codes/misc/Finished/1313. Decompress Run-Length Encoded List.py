# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums):
        xlist = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                xlist.append(nums[i+1])
        return xlist