from ast import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        output = []
        for i, j in zip(x, y):
            output.append(i)
            output.append(j)
        return output