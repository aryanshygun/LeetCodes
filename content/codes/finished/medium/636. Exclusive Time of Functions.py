from _ast import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        prev_time = 0
        result = [0] * n
        stack = []
        for i in logs:
            part = i.split(":")
            if (part[1]) == "start":
                if stack:
                    result[stack[-1]] += int(part[2]) - prev_time
                stack.append(int(part[0]))
                prev_time = int(part[2])
            else:
                result[stack[-1]] += int(part[2]) - prev_time + 1
                prev_time = int(part[2]) + 1
                stack.pop()
        return result
