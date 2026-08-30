class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = i
        count = 0
        x = []
        while j < len(s):
            if s[j] not in x:
                x.append(s[j])
                j += 1
            elif s[j] in x or len(s) > 150:
                x.remove(s[i])
                i += 1
                continue

            count = max(count, len(x))
        return count

