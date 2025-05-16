from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        """
        approach
        sort spaces
        from the back of the sthring, iterate with i
        when i == top of spaces
        add a space
        pop top of spaces
        continue
        at the end, the spaces have been inserted in place
        """
        spaces = sorted(spaces)
        n = len(s)
        builder = []
        for i in range(n - 1, -1, -1):
            builder.append(s[i])
            if spaces and i == spaces[-1]:
                builder.append(" ")
                spaces.pop()
        return "".join(reversed(builder))
