# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'AaEeIiOoUu'
        xlist = [*s]
        l, r = 0, len(xlist) - 1
        while l < r:
            if xlist[l] not in vowels:
                l += 1
            elif xlist[r] not in vowels:
                r -= 1
            else:
                xlist[l], xlist[r] = xlist[r], xlist[l]
                l += 1
                r -= 1      
        return ''.join(xlist)
