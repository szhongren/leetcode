from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        approach:
        go through the grid one by one, if value == 0, add x to zero, y to zero
        """
        to_zero_x = set()
        to_zero_y = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    to_zero_x.add(i)
                    to_zero_y.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in to_zero_x or j in to_zero_y:
                    matrix[i][j] = 0
