"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        curr = 1
        half = (n + 1) // 2
        for layer in range(half):
            for x in range(layer, layer + 1):
                for y in range(layer, n - layer - 1):
                    res[x][y] = curr
                    curr += 1
            for x in range(layer, n - layer - 1):
                for y in range(n - layer - 1, n - layer):
                    res[x][y] = curr
                    curr += 1
            for x in range(n - layer - 1, n - layer):
                for y in range(n - layer - 1, layer, -1):
                    res[x][y] = curr
                    curr += 1
            for x in range(n - layer - 1, layer, -1):
                for y in range(layer, layer + 1):
                    res[x][y] = curr
                    curr += 1
        if n % 2:
            res[half - 1][half - 1] = curr
        return res

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        half_m = (m + 1) // 2
        half_n = (n + 1) // 2
        ans = []
        for layer in range(min(half_m, half_n)):
            for x in range(layer, layer + 1):
                for y in range(layer, n - layer - 1):
                    ans.append(matrix[x][y])
            for x in range(layer, m - layer - 1):
                for y in range(n - layer - 1, n - layer):
                    ans.append(matrix[x][y])
            for x in range(m - layer - 1, m - layer):
                for y in range(n - layer - 1, layer, -1):
                    ans.append(matrix[x][y])
            for x in range(m - layer - 1, layer, -1):
                for y in range(layer, layer + 1):
                    ans.append(matrix[x][y])
        # if n % 2:
        #     ans.append(matrix[half_m - 1][half_n - 1])
        if m % 2 and n % 2:
            if m == n:
                ans.append(matrix[half_m - 1][half_n - 1])
            else:
                ans.pop()
        return ans

ans = Solution()
for i in range(8):
    print(i)
    mat = ans.generateMatrix(i)
    for row in mat:
        print(row)
    print(ans.spiralOrder(mat))
    print()

print(ans.spiralOrder([
    [1]
]))
print(ans.spiralOrder([
    [1],
    [2],
    [3]
]))
print(ans.spiralOrder([
    [1, 2, 3, 4, 5],
    [12, 13, 14, 15, 6],
    [11, 10, 9, 8, 7]
]))
# odd odd
print(ans.spiralOrder([
    [1, 2],
    [6, 3],
    [5, 4]
]))
# odd even
print(ans.spiralOrder([
    [1, 2, 3],
    [10, 11, 4],
    [9, 12, 5],
    [8, 7, 6]
]))
# even odd
print(ans.spiralOrder([
    [1, 2, 3, 4],
    [16, 17, 18, 5],
    [15, 24, 19, 6],
    [14, 23, 20, 7],
    [13, 22, 21, 8],
    [12, 11, 10, 9],
]))
# even even
