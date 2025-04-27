from collections import deque


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        approach:
        recursion
        base case: 1 char or ""
        else:
        check first and last char
        if equal
        recur without first and last
        else if still have remove available
        recur with removing first or last
        """

        def validPalindromeRecur(s: deque, can_remove: bool) -> bool:
            if len(s) <= 1:
                return True
            if s[0] == s[-1]:
                last = s.pop()
                first = s.popleft()
                if validPalindromeRecur(s, can_remove):
                    return True
                s.appendleft(first)
                s.append(last)
            else:
                if can_remove:
                    last = s.pop()
                    if validPalindromeRecur(s, False):
                        return True
                    s.append(last)
                    s.popleft()
                    if validPalindromeRecur(s, False):
                        return True
                return False

        return validPalindromeRecur(deque(s), True)


sol = Solution()
sol.validPalindrome("eceec")
