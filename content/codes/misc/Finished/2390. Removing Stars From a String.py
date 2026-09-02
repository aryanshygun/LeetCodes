# https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        x = []
        for i in s:
            if i is '*':
                x.pop()
            else:
                x.append(i)
        return ''.join(x)