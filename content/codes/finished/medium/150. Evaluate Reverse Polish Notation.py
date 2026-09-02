from ast import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue

            a, b = stack[-2], stack[-1]
            match token:
                case "+":
                    result = a + b
                case "-":
                    result = a - b
                case "*":
                    result = a * b
                case "/":
                    result = int(a / b)
            stack.pop()
            stack[-1] = result
        return stack[0]
