# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/?envType=daily-question&envId=2024-03-29

class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        x = ''.join(i for i in word1)
        y = ''.join(i for i in word2)
        return x == y