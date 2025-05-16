class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        2d dp
        1 more to deal with empty string
            a b c
          0 1 2 3
        d 1 2
        e 2
        f 3

            a b c
          0 1 2 3
        a 1 0 1 2
        b 2 1 0 1
        b 3 2 1 1
        f 4
        rules:
        if !=, min [i-1][j-1] + 1, [i-1][j] + 1, [i][j - 1] + 1
        if ==, min [i-1][j-1], [i-1][j] + 1, [i][j - 1] + 1
        """
        m = len(word1)
        n = len(word2)
        if m == 0:
            return n
        if n == 0:
            return m
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                should_edit = False
                if word1[i - 1] != word2[j - 1]:
                    should_edit = True
                dp[i][j] = min(
                    dp[i - 1][j - 1] + (1 if should_edit else 0),
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                )
        print(dp)
        return dp[-1][-1]


sol = Solution()
sol.minDistance("a", "b")
