# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        inta = int(a, 2)
        intb = int(b, 2)
        c = inta + intb
        return bin(c)[2::]