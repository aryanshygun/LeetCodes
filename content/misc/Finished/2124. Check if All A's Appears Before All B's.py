# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/


class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' in s:
            if 'a' in s[s.index('b')::]:
                return False
            return True
        return True