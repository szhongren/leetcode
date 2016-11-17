"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x = 0
        y = 0
        found_row = False
        while True:
            if x == len(matrix):
                return False
            elif found_row:
                if matrix[x][y] > target:
                    return False
                elif matrix[x][y] == target:
                    return True
                else:
                    y += 1
            elif not found_row:
                if matrix[x][-1] < target:
                    x += 1
                else:
                    found_row = True