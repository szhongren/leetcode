from pprint import pprint


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         max_len = 1
#         palindrome = s[0]
#         cache = {}

#         def isPalindromeRecur(a: int, b: int) -> int:
#             nonlocal max_len
#             nonlocal palindrome
#             if (a, b) in cache:
#                 return cache[(a, b)]
#             if a == b - 1:
#                 cache[(a, b)] = True
#                 return True
#             if a == b - 2:
#                 result = s[a] == s[b - 1]
#                 cache[(a, b)] = result
#                 if result and 2 > max_len:
#                     max_len = 2
#                     palindrome = s[a:b]
#                 return result
#             sub_string_result = s[a] == s[b - 1] and isPalindromeRecur(a + 1, b - 1)
#             cache[(a, b)] = sub_string_result
#             if sub_string_result and b - a > max_len:
#                 max_len = b - a
#                 palindrome = s[a:b]
#             return sub_string_result

#         for i in range(len(s) + 1):
#             for j in range(i + 1, len(s) + 1):
#                 isPalindromeRecur(i, j)
#         return palindrome


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start = end = 0
        for i in range(len(s)):
            # Check odd length palindromes
            l1, r1 = expand_around_center(i, i)
            if r1 - l1 > end - start:
                start, end = l1, r1

            # Check even length palindromes
            l2, r2 = expand_around_center(i, i + 1)
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("racecar"))
print(sol.longestPalindrome("racecart"))
print(sol.longestPalindrome("raceecart"))
