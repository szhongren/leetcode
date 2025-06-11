from typing import List
from pprint import pprint


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

         0 1 2
        0
        1
        2

        0, 0
        0, 2
        2, 2
        2, 0

        0, 1
        1, 2
        2, 1
        1, 0

         0 1 2 3
        0
        1
        2
        3

        0, 0
        3, 0
        3, 3
        0, 3

        0, 1
        2, 0
        3, 2
        1, 3

        """
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp


ans = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(mat)
ans.rotate(mat)
pprint(mat)
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
pprint(mat2)
ans.rotate(mat2)
pprint(mat2)
mat3 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
pprint(mat3)
ans.rotate(mat3)
pprint(mat3)
