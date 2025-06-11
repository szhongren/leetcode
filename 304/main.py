from typing import List
from pprint import pprint


class NumMatrix:
    """
    approach
    for every position in the matrix, get the sum of the box from the origin to that point and store it in the matrix
    for every sumRegion call, return sum[bot_right] - sum[bot_left] - sum[top_right] + sum[top_left]
    """

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] * len(row) for row in matrix]
        self.sums[0][0] = matrix[0][0]
        for i in range(1, len(matrix)):
            self.sums[i][0] = self.sums[i - 1][0] + matrix[i][0]
        for j in range(1, len(matrix[0])):
            self.sums[0][j] = self.sums[0][j - 1] + matrix[0][j]
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.sums[i][j] = (
                    self.sums[i - 1][j]
                    + self.sums[i][j - 1]
                    - self.sums[i - 1][j - 1]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.sums[row2][col2]
        elif row1 == 0:
            return self.sums[row2][col2] - self.sums[row2][col1 - 1]
        elif col1 == 0:
            return self.sums[row2][col2] - self.sums[row1 - 1][col2]
        else:
            return (
                self.sums[row2][col2]
                - self.sums[row1 - 1][col2]
                - self.sums[row2][col1 - 1]
                + self.sums[row1 - 1][col1 - 1]
            )


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
ans = NumMatrix(
    [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
)
print(ans.sumRegion(0, 0, 2, 3))
print(ans.sumRegion(2, 1, 4, 3))
print(ans.sumRegion(1, 1, 2, 2))
print(ans.sumRegion(1, 2, 2, 4))
