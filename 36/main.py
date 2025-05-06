from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        approach
        for every row, every col, every sq, have a set
        iterate through the list, if value already in set, return false
        else add
        at end, return True
        """
        col_sets = {n: set() for n in range(9)}
        row_sets = {n: set() for n in range(9)}
        sq_sets = {(a, b): set() for a in [0, 1, 2] for b in [0, 1, 2]}

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if (
                    value in col_sets[i]
                    or value in row_sets[j]
                    or value in sq_sets[(i // 3, j // 3)]
                ):
                    return False
                col_sets[i].add(value)
                row_sets[j].add(value)
                sq_sets[(i // 3, j // 3)].add(value)
        return True
        """
         0 1 2 3 4 5 6 7 8
        0
        1
        2
        3
        4
        5
        6
        7
        8
        """
