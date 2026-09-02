from typing import list


class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        result = []
        for i in order:
            if i in friends:
                result.append(i)
        return result
