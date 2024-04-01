# https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices) -> str:
        result = [None] * len(s)
        for char, index in zip(s, indices):
            result[index] = char
        return ''.join(result)