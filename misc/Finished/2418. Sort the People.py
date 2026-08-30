# https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names, heights):
        xlist = [[i,j] for i,j in zip(names, heights)]
        xlist = sorted(xlist, key=lambda x: x[1], reverse=True)
        return [i[0] for i in xlist]