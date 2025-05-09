# class Solution:
#     def isOneEditDistance(self, s: str, t: str) -> bool:
#         """
#         approach
#         do edit distance dp
#         if s[i] == s[j], dp[i][j] = min(dp[i-1][j-1], dp[i-i][j], dp[i][j-1])
#         if s[i] != s[j], dp[i][j] = min(dp[i-1][j-1], dp[i-i][j], dp[i][j-1]) + 1
#             a b c
#           0 0 0 0
#         a 0 0 1 2
#         b 0 1 0 1
#         i 0 2 1 1
#         c 0 3 2 1
#         """
#         m = len(s)
#         n = len(t)
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
#         for i in range(1, m + 1):
#             dp[i][0] = i
#         for i in range(1, n + 1):
#             dp[0][i] = i
#         for i in range(1, m + 1):
#             for j in range(1, n + 1):
#                 smallest = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
#                 if s[i - 1] == t[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]  # No cost for matching characters
#                 else:
#                     dp[i][j] = smallest + 1
#         return dp[-1][-1] == 1


class Solution:
    def isOneEditDistance(self, s: "str", t: "str") -> "bool":
        ns, nt = len(s), len(t)

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # The strings are NOT one edit away from distance
        # if the length diff is more than 1.
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # If strings have the same length
                if ns == nt:
                    return s[i + 1 :] == t[i + 1 :]
                # If strings have different lengths
                else:
                    return s[i:] == t[i + 1 :]

        # If there are no diffs in ns distance
        # The strings are one edit away only if
        # t has one more character.
        return ns + 1 == nt
