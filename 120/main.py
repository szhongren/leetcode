from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        approach
        bottom up dp, because we end up with 1 value at the top
        for each level above the bottom, set value == min(bottom left, bottom right) + current
        return triangle[0][0]

        edge cases
        0 levels -> not possible
        1 level -> return only value
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


"""
1

1
2 3
1 4 8

4
3 7
1 4 8

"""
