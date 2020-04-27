"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        remaining_pos = {(i, j): 0 for i in range(9) for j in range(9)}
        possible_values = [[{i: 1 for i in "123456789"} for _ in range(9)] for _ in range(9)]

        # setup
        for x in range(9):
            for y in range(9):
                ch = board[x][y]
                if ch == '.':
                    continue
                possible_values[x][y][ch] = 0
                del remaining_pos[(x, y)]
                for i in range(9):
                    possible_values[x][i][ch] = 0
                for i in range(9):
                    possible_values[i][y][ch] = 0
                sector_x = x // 3
                sector_y = y // 3
                for i in range(sector_x, sector_x + 3):
                    for j in range(sector_y, sector_y + 3):
                        possible_values[i][j][ch] = 0
        for cell in remaining_pos.keys():
            x = cell[0]
            y = cell[1]
            if board[x][y] != '.':
                return False
        for row in possible_values:
            print(row)
        print(remaining_pos)

ans = Solution()
board = [
    "..9748...",
    "7........",
    ".2.1.9...",
    "..7...24.",
    ".64.1.59.",
    ".98...3..",
    "...8.3.2.",
    "........6",
    "...2759.."
]
print(ans.solveSudoku(board))
print(board)
