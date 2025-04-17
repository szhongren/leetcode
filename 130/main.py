from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        approach, dfs from every cell on edge
        remove every cell we can reach
        done
        """
        cells_to_check = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    cells_to_check.add((i, j))
        edge_cells = [
            (i, j)
            for (i, j) in cells_to_check
            if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1
        ]

        def bfs(i, j):
            if (i, j) not in cells_to_check:
                # do nothing
                return
            cells_to_check.remove((i, j))
            bfs(i - 1, j)
            bfs(i + 1, j)
            bfs(i, j - 1)
            bfs(i, j + 1)

        for edge_cell in edge_cells:
            bfs(*edge_cell)
        for i, j in cells_to_check:
            board[i][j] = "X"


sol = Solution()
sol.solve(
    [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
)
