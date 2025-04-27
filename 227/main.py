from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """
        approach
        use stack, if has precedence, evaluate immediately, otherwise evaluate later
        """
        stack = deque()
        s_without_spaces = s.replace(" ", "")
        i = 0
        j = 0
        while i < len(s_without_spaces):
            if j >= len(s_without_spaces):
                previous_number = int(s_without_spaces[i:j])
                if len(stack) > 0 and (stack[-1] == "*" or stack[-1] == "/"):
                    # early compute
                    op = stack.pop()
                    value = stack.pop()
                    if op == "*":
                        previous_number = previous_number * value
                    elif op == "/":
                        previous_number = int(value / previous_number)
                stack.append(previous_number)
                break
            elif s_without_spaces[j].isdigit():
                j += 1
            else:
                previous_number = int(s_without_spaces[i:j])
                if len(stack) > 0 and (stack[-1] == "*" or stack[-1] == "/"):
                    # early compute
                    op = stack.pop()
                    value = stack.pop()
                    if op == "*":
                        previous_number = previous_number * value
                    elif op == "/":
                        previous_number = int(value / previous_number)
                operation = s_without_spaces[j]
                i = j + 1
                j = i
                stack.append(previous_number)
                stack.append(operation)
        while len(stack) != 1:
            a = stack.popleft()
            op = stack.popleft()
            b = stack.popleft()
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
