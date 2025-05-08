class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        approach
        recursive
        with i, running_count
        if at end, return running_count == 0
        if at any point, running count is negative, return false
        if current == *, branch and return true if any are true
        """

        n = len(s)

        cache = {}

        def checkValidStringRecur(i: int, acc: int) -> bool:
            if (i, acc) in cache:
                return cache[(i, acc)]
            if i == n:
                cache[(i, acc)] = acc == 0
                return cache[(i, acc)]
            if acc < 0:
                cache[(i, acc)] = False
                return cache[(i, acc)]
            ch = s[i]
            if ch == "(":
                cache[(i, acc)] = checkValidStringRecur(i + 1, acc + 1)
                return cache[(i, acc)]
            elif ch == ")":
                cache[(i, acc)] = checkValidStringRecur(i + 1, acc - 1)
                return cache[(i, acc)]
            elif ch == "*":
                cache[(i, acc)] = any(
                    [
                        checkValidStringRecur(i + 1, acc + 1),
                        checkValidStringRecur(i + 1, acc),
                        checkValidStringRecur(i + 1, acc - 1),
                    ]
                )
                return cache[(i, acc)]

        return checkValidStringRecur(0, 0)
