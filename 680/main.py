class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        approach
        recursive
        base case:
        if len(s) == 1 or 0 or 2:
        return true
        else
        if front and back are equal, return recur(s[1:-1])
        if not equal, return recur(s[:-1]) or recur(s[1:])
        have flag for whether delete has been used
        """

        def validPalindromeRecur(start: int, end: int, can_delete: bool) -> bool:
            if start > end:
                return True
            if start == end:
                return True
            if s[start] != s[end]:
                if can_delete:
                    return validPalindromeRecur(
                        start + 1, end, False
                    ) or validPalindromeRecur(start, end - 1, False)
                else:
                    return False
            return validPalindromeRecur(start + 1, end - 1, can_delete)

        return validPalindromeRecur(0, len(s) - 1, True)
