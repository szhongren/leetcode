class Solution:
    def isValid(self, s: str) -> bool:
        """
        approach
        use a stack, if open, push onto stack
        if close, if not matching on stack, return False
        else, pop and continue
        return True if ended
        """
        stack = []
        for ch in s:
            if ch in ("(", "{", "["):
                stack.append(ch)
            elif ch == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif ch == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif ch == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
