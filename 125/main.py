from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = [c.lower() for c in s if c.isalnum()]

        def isPalindromeRecur(a: int, b: int):
            print(
                f"a: {a}, s[a]: {cleaned_string[a]}, b: {b}, s[b]: {cleaned_string[b]}"
            )
            if b - a < 1:
                return True
            if cleaned_string[a] != cleaned_string[b]:
                return False
            return isPalindromeRecur(a + 1, b - 1)

        return isPalindromeRecur(0, len(cleaned_string) - 1)


sol = Solution()
sol.isPalindrome("race a car")
