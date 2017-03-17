"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.findTargetSumWaysRecur(nums, 0, S, {0: 1})

    def findTargetSumWaysRecur(self, nums, pos, S, ways):
        if pos == len(nums):
            if S in ways:
                return ways[S]
            return 0

        new_ways = {}
        curr = nums[pos]
        for k, v in ways.items():
            for i in [-1, 1]:
                if k + i * curr in new_ways:
                    new_ways[k + i * curr] += v
                else:
                    new_ways[k + i * curr] = v
        return self.findTargetSumWaysRecur(nums, pos + 1, S, new_ways)

ans = Solution()
print(ans.findTargetSumWays([1, 1, 1, 1, 1], 3))
