# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/

class Solution:
    def garbageCollection(self, garbage, travel):

        pmin, l = 0, 0
        pmax = max((i for i, string in enumerate(garbage) if 'P' in string), default=0)
        while l < pmax:
            pmin += garbage[l].count('P') + travel[l]
            l += 1
        else:
            pmin += garbage[l].count('P')
        
        mmin, l = 0, 0
        mmax = max((i for i, string in enumerate(garbage) if 'M' in string), default=0)
        while l < mmax:
            mmin += garbage[l].count('M') + travel[l]
            l += 1
        else:
            mmin += garbage[l].count('M')
        
        gmin, l = 0, 0
        gmax = max((i for i, string in enumerate(garbage) if 'G' in string), default=0)
        while l < gmax:
            gmin += garbage[l].count('G') + travel[l]
            l += 1
        else:
            gmin += garbage[l].count('G')
            
        return pmin + gmin + mmin
        
    

garbage = ["G","P","GP","GG"]


travel = [2,4,3]
# 8 13 = 21
x = Solution()
print(x.garbageCollection(garbage, travel))
