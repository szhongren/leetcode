"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        add = 1
        element_count = 0
        cols = len(matrix[0])
        rows = len(matrix)
        potential_a = 100000000
        potential_b = 100000000
        if k <= cols:
            potential_a = matrix[0][k - 1]
        if k <= rows:
            potential_b = matrix[k - 1][0]
        if k == cols * rows:
            return matrix[-1][-1]
        if k == 1:
            return matrix[0][0]
        while element_count < k:
            element_count += add - (add - min(add, cols)) - (add - min(add, rows))
            add += 1
        add -= 2
        offset_i = element_count - k
        results = []
        for i in range(add + 1):
            j = add - i
            if i < rows and j < cols:
                results.append(matrix[i][j])
        return min(sorted(results)[offset_i - 1], potential_a, potential_b)

ans = Solution()
# print(ans.kthSmallest(
# [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ], 8))
# print(ans.kthSmallest([[1,2],[1,3]], 2))
print(ans.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 3))