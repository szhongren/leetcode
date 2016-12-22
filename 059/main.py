"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        for layer in range(n // 2):
            for i in range(n - 2 * layer - 1):
                res[layer][layer + i] = 1
        return res

"""
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
"""

ans = Solution()
for i in range(8):
    print(i)
    for row in ans.generateMatrix(i):
        print(row)
    print()