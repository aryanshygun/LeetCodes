# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        xdict = {'X--':0,'--X':0, 'X++':0,'++X':0}
        for i in operations:
            xdict[i] = xdict.get(i, 0) + 1
        

        return xdict['X++'] + xdict['++X'] - xdict['--X'] - xdict['X--']