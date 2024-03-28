# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        xlist = [int(i) for i in s.split() if i.isdigit()]
        return xlist == list(sorted(set(xlist)))