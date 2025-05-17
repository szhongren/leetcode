from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        approach
        for every col, for every row, for every box, have a set of used digits
        iterate through every cell, if digit already in set, return False
        return True at the end
         0 1 2 3 4 5 6 7 8 9
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
        """
        col_sets = {n: set() for n in range(9)}
        row_sets = {n: set() for n in range(9)}
        # i and j both // 3, will return 0, 1, 2
        sq_sets = {(a, b): set() for a in range(3) for b in range(3)}
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in row_sets[i]:
                    return False
                row_sets[i].add(cell)
                if cell in col_sets[j]:
                    return False
                col_sets[j].add(cell)
                if cell in sq_sets[(i // 3, j // 3)]:
                    return False
                sq_sets[(i // 3, j // 3)].add(cell)
        return True
