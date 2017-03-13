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
        return 0

ans = Solution()
print(ans.kthSmallest(
[
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8))
print(ans.kthSmallest([[1,2],[1,3]], 2))
print(ans.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 3))
