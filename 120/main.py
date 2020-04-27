"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        triangle[0] = 3 * triangle[0]
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row - 1][col], triangle[row - 1][col + 1])
            triangle[row] = [triangle[row][0]] + triangle[row] + [triangle[row][-1]]
        return min(triangle[-1][1:-1])

ans = Solution()
print(ans.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
print(ans.minimumTotal([[-10]]))