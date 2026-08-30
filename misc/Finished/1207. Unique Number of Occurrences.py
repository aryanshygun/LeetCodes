# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        xdict = {}
        for i in arr:
            xdict[i] = xdict.get(i, 0) + 1
        return len(xdict.values()) == len(set(xdict.values()))