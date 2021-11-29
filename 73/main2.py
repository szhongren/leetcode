from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns_to_set = set()
        rows_to_set = set()
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == 0:
                    columns_to_set.add(j)
                    rows_to_set.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows_to_set or j in columns_to_set:
                    matrix[i][j] = 0
