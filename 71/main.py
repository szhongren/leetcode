from typing import Tuple


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        approach:
        use a stack
        / does nothing if last on stack is /
        ./ does nothing
        ../ will pop
        otherwise push
        """

        def substr_to_slash(s: str, index: int) -> Tuple[str, int]:
            slash_index = s.find("/", index)
            if slash_index == -1:
                return s[index:], len(s)
            else:
                return s[index:slash_index], slash_index

        stack = ["/"]
        index = 1
        while index < len(path):
            if path[index] == "/":
                if stack[-1] != "/":
                    stack.append("/")
                index += 1
            else:
                path_part, slash_index = substr_to_slash(path, index)
                if path_part == ".":
                    pass
                elif path_part == "..":
                    if len(stack) > 1:
                        stack.pop()
                        stack.pop()
                else:
                    stack.append(path_part)
                index = slash_index
        if stack[-1] == "/" and len(stack) > 1:
            stack.pop()
        return "".join(stack)
