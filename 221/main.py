"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        sizes = [[int(bit) for bit in row] for row in matrix]
        side = 0
        for x in range(len(sizes)):
            for y in range(len(sizes[0])):
                if sizes[x][y] == 0:
                    continue
                if x == 0 or y == 0:
                    side = max(1, side)
                    continue
                sizes[x][y] = min(sizes[x - 1][y - 1], sizes[x - 1][y], sizes[x][y - 1]) + 1
                side = max(side, sizes[x][y])
                # prev = sizes[x - 1][y - 1]
                # if prev == 0:
                #     continue
                # for side in range(1, prev + 1):
                #     up = [sizes[i][y] for i in range(x - side, x)]
                #     if 0 in up:
                #         continue
                #     left = [sizes[x][i] for i in range(y - side, y)]
                #     if 0 in left:
                #         continue
                #     sizes[x][y] = side + 1
        return side * side

ans = Solution()
print(ans.maximalSquare([
    "00010",
    "11010",
    "11111",
    "01111",
    "01111",
    "01111"
]))
print(ans.maximalSquare([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))

print(ans.maximalSquare([
    [],
    [],
    []
]))

print(ans.maximalSquare([]))
