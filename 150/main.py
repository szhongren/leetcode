from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        approach
        stack based
        if number, push onto stack, else, take last 2, and calculate, and push onto stack
        """
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b, a = stack.pop(), stack.pop()
                result = None
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]
