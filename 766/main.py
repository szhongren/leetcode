from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        insight: diagonals have same x - y difference, so matrix[x][y] should have the same value as matrix[a][b] where x - y = a - b
        """
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if x == 0 or y == 0:
                    # this is the base, don't need to check
                    continue
                difference = y - x
                """
                negative numbers are top row
                positive numbers are left col
                """
                if difference == 0:
                    if matrix[x][y] != matrix[0][0]:
                        return False
                elif difference > 0:
                    if matrix[x][y] != matrix[0][abs(difference)]:
                        return False
                else:
                    if matrix[x][y] != matrix[abs(difference)][0]:
                        return False
        return True
