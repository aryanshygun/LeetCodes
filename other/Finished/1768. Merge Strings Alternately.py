# https://leetcode.com/problems/merge-strings-alternately/submissions/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            min = len(word2)
        else:
            min = len(word1)
        x = ''
        for i in range(min):
            x += word1[i] + word2[i]
        x += word1[min::] + word2[min::]
        return x