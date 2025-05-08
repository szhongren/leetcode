from typing import List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        approach
        backtracking
        for each cell, if start of word
        start dfs
        dfs, at each point
        look at neighbors not already used
        if empty string to match, return true

        edge cases:
        [[a b c d]]
        [[b a a a]], aaab
        baaa
        """
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, word: str, seen: Set[int]):
            if word == "":
                return True
            if len(word) == 1 and board[i][j] == word[-1]:
                return True
            if word[-1] != board[i][j]:
                return False
            seen.add((i, j))
            # look up
            if i > 0 and (i - 1, j) not in seen and dfs(i - 1, j, word[:-1], seen):
                return True
            # look down
            if i < m - 1 and (i + 1, j) not in seen and dfs(i + 1, j, word[:-1], seen):
                return True
            # look right
            if j < n - 1 and (i, j + 1) not in seen and dfs(i, j + 1, word[:-1], seen):
                return True
            # look left
            if j > 0 and (i, j - 1) not in seen and dfs(i, j - 1, word[:-1], seen):
                return True
            seen.remove((i, j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, word[::-1], set()):
                        return True
        return False


sol = Solution()
sol.exist([["a", "a"]], "aaa")
