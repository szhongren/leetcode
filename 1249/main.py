class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        approach:
        go char by char, append to result
        if not (), just append
        if (, continue and wait for matching )
        """

        def minRemoveToMakeValid(s: str, opened: bool):
            if s == "":
                return ""
            if s[0] not in ["(", ")"]:
                return s + minRemoveToMakeValid(s[1:])

        return minRemoveToMakeValid(s, False)
