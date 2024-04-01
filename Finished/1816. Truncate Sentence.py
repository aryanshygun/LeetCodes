# https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        xlist = []
        for i in range(k):
            xlist.append(s.split()[i])
        return ' '.join(xlist)