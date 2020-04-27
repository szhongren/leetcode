"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"

Output:

4

One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:

"cbbd"

Output:

2

One possible longest palindromic subsequence is "bb".
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        def f(s):
            if s not in d:
                max_length = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    max_length = max(max_length, 1 if i == j else 2 + f(s[i + 1:j]))
                d[s] = max_length
            return d[s]
        return f(s)
        # l = len(s)
        # dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]
        # rev = s[::-1]
        # for i in range(1, l + 1):
        #     for j in range(1, l + 1):
        #         dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (s[i - 1] == rev[j - 1]))
        # return dp[-1][-1]

ans = Solution()
print(ans.longestPalindromeSubseq("bbbab"))
print(ans.longestPalindromeSubseq("cbbd"))
