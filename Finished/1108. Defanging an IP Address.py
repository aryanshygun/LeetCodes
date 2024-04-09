# https://leetcode.com/problems/defanging-an-ip-address/submissions/1225171009/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        x = [*address]
        for i in range(len(x)):
            if x[i] == '.':
                x[i] = '[.]'
        return ''.join(x)