from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        approach
        sort by sum of indices, then by y
        first diagonal, sum of 0
        second diagonal, sum of 1
        etc
        so, create a list of tuples, (sum, y, x)
        sort
        read values in order
        """
        visit_order = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                visit_order.append((i + j, j, i))

        visit_order.sort()
        result = []
        for _, y, x in visit_order:
            result.append(nums[x][y])
        return result
