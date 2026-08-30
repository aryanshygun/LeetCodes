from typing import list


class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        min_list = [min(i) for i in arrays]
        max_list = [max(i) for i in arrays]

        min_list_2 = min_list[:]
        max_list_2 = max_list[:]

        x_max = max(max_list)
        min_list.pop(max_list.index(x_max))
        x_min = min(min_list)

        x_min_2 = min(min_list_2)
        max_list_2.pop(min_list_2.index(x_min_2))
        x_max_2 = max(max_list_2)

        return max(x_max_2 - x_min_2, x_max - x_min)
