class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        approach
        use stack
        if "." do nothing
        if ".." pop
        if "/" push if not "/" on top, else, do nothing
        """
        stack = ["/"]
        i = 1
        n = len(path)

        def get_next_part(i: int):
            if i >= n:
                return None
            if path[i] == "/":
                i += 1
                return (i, "/")
            else:
                j = i
                while j < n and path[j] != "/":
                    j += 1
                return (j, path[i:j])

        while i < n:
            i, part = get_next_part(i)
            if part == ".":
                continue
            elif part == "..":
                if len(stack) < 3:
                    continue
                stack.pop()
                stack.pop()
                continue
            elif part == "/":
                if stack[-1] == "/":
                    continue
            stack.append(part)
        if len(stack) != 1 and stack[-1] == "/":
            stack.pop()
        return "".join(stack)
