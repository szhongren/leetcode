from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """
        approach
        use stack, if has precedence, evaluate immediately, otherwise evaluate later
        """
        stack = deque()
        i = 0
        s = s.replace(" ", "")
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                current_number = 0
                while i < n and s[i].isdigit():
                    current_number *= 10
                    current_number += int(s[i])
                    i += 1
                stack.append(current_number)
                if len(stack) < 3:
                    continue
                operator = stack[-2]
                if operator == "*":
                    b, _, a = stack.pop(), stack.pop(), stack.pop()
                    stack.append(b * a)
                elif operator == "/":
                    b, _, a = stack.pop(), stack.pop(), stack.pop()
                    stack.append(a // b)
            else:
                stack.append(ch)
                i += 1
        while len(stack) != 1:
            a, op, b = stack.popleft(), stack.popleft(), stack.popleft()
            if op == "+":
                stack.appendleft(a + b)
            elif op == "-":
                stack.appendleft(a - b)
        return stack[0]


sol = Solution()
print(sol.calculate("3+2*2"))
print(sol.calculate(" 3/2 "))
print(sol.calculate(" 3+5 / 2 "))
print(sol.calculate("1-1+1"))
