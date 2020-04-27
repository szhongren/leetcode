"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = min(nums)
        result = 0
        for v in nums:
            result += v - smallest
        return result


ans = Solution()
print(ans.minMoves([1,2,3]))