"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
import math

def median(ls):
    length = len(ls)
    half_length = length // 2
    if length % 2 == 0:
        return sum(ls[half_length - 1: half_length + 1])/2
    else:
        return ls[half_length]

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        med = median(nums)
        moves = 0
        for v in nums:
            moves += abs(v - med)
        return moves

ans = Solution()
print(ans.minMoves2([1,2,3]))