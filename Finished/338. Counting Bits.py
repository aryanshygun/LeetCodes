# https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def countBits(self, n):
        xlist = []
        index = 0
        while index < n + 1:
            bin_index = bin(index)[2::]
            xlist.append(bin_index.count('1'))
            index += 1
        return xlist

