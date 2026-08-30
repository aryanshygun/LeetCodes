class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1

        n = 0
        while j < len(s):
            a = ord(s[i])
            b = ord(s[j])
            n += abs(a - b)
            i += 1
            j += 1
        return n
