from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        approach
        0 0
        0 1, 1 0
        2 0, 1 1, 0 2
        sum(x, y) is even or odd for every diagonal
        generate all xy, sort by x if sum % 2 == 1, else sort by y
        O(mn + mnlg(mn))
        """
        m = len(mat)
        n = len(mat[0])
        coords = []
        for i in range(m):
            for j in range(n):
                coords.append((i + j, i, j))
        coords.sort(
            key=lambda sumxy: (sumxy[0], sumxy[1] if sumxy[0] % 2 == 1 else sumxy[2])
        )
        result = []
        for _, x, y in coords:
            result.append(mat[x][y])
        return result
