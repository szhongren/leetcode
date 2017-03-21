"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input:

0 0 0
0 1 0
0 0 0

Output:

0 0 0
0 1 0
0 0 0

Example 2:
Input:

0 0 0
0 1 0
1 1 1

Output:

0 0 0
0 1 0
1 2 1

Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        indexes = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 1]
        matrix = [[0 if val == 0 else -1 for val in row]for row in matrix]
        curr_level = 0
        while len(indexes) > 0:
            new_indexes = []
            for index in indexes:
                done = False
                x = index[0]
                y = index[1]
                if x > 0:
                    if matrix[x - 1][y] == curr_level:
                        done = True
                        matrix[x][y] = curr_level + 1
                if y > 0:
                    if matrix[x][y - 1] == curr_level:
                        done = True
                        matrix[x][y] = curr_level + 1
                if x < len(matrix) - 1:
                    if matrix[x + 1][y] == curr_level:
                        done = True
                        matrix[x][y] = curr_level + 1
                if y < len(matrix[0]) - 1:
                    if matrix[x][y + 1] == curr_level:
                        done = True
                        matrix[x][y] = curr_level + 1
                if not done:
                    new_indexes.append(index)
            curr_level += 1
            indexes = new_indexes
        return matrix

ans = Solution()
print(ans.updateMatrix([
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]))
print(ans.updateMatrix([
    [1, 1, 1],
    [0, 1, 0],
    [0, 0, 0]
]))

