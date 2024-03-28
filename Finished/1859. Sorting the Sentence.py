# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s = sorted(s.split(), key=lambda x:x[-1])
        return ' '.join(i[:-1] for i in s)