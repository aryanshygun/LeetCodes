# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        s = max(candies)
        return [x + extraCandies >= s for x in candies]
