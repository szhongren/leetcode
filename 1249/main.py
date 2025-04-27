class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        approach
        do a count, ( += 1, ) -= 1
        """
        counter = 0
        to_remove = set()
        for i, char in enumerate(s):
            if char == "(":
                counter += 1
            elif char == ")":
                if counter == 0:
                    to_remove.add(i)
                    continue
                counter -= 1
        counter = 0
        for i, char in enumerate(s[::-1]):
            if char == ")":
                counter += 1
            elif char == "(":
                if counter == 0:
                    to_remove.add(len(s) - i - 1)
                    continue
                counter -= 1
        return "".join([ch for i, ch in enumerate(s) if i not in to_remove])


sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))
print(sol.minRemoveToMakeValid("a)b(c)d"))
print(sol.minRemoveToMakeValid("))(("))
