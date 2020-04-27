"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [0] * (rowIndex + 2)
        row[1] = 1
        for i in range(rowIndex):
            new_row = [0] * (rowIndex + 2)
            for j in range(1, rowIndex + 2):
                new_row[j] = row[j - 1] + row[j]
            row = new_row
        return row[1:]

ans = Solution()
print(ans.getRow(4))