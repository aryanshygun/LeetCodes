from ast import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []
        i = 0

        while i < len(temperatures):
            temp = temperatures[i]

            while stack and temp > temperatures[stack[-1]]:
                previous = stack.pop()
                output[previous] = i - previous

            stack.append(i)
            i += 1

        return output
