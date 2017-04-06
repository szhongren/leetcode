"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

    Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:

    Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board
        def countLiveNeighbors(x, y):
            count = 0
            for i in range(max(0, x - 1), min(len(board), x + 2)):
                for j in range(max(0, y - 1), min(len(board[0]), y + 2)):
                    if i == x and j == y:
                        continue
                    count += board[i][j]
            return count
        live = [(x, y) for x, a in enumerate(board) for y, b in enumerate(a) if b == 1]
        dead = [(x, y) for x, a in enumerate(board) for y, b in enumerate(a) if b == 0]
        new_live = []
        new_dead = []
        for cell in live:
            neighbors = countLiveNeighbors(cell[0], cell[1])
            if neighbors < 2:
                new_dead.append(cell)
            elif neighbors < 4:
                continue
            else:
                new_dead.append(cell)
        for cell in dead:
            neighbors = countLiveNeighbors(cell[0], cell[1])
            if neighbors == 3:
                new_live.append(cell)
        for cell in new_live:
            board[cell[0]][cell[1]] = 1
        for cell in new_dead:
            board[cell[0]][cell[1]] = 0
        return board

ans = Solution()
print(ans.gameOfLife([[1,1],[1,0]]))
