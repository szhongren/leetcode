"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = nums[0]
        # max_i = 0
        # backtrack = [False for _ in range(len(nums))]
        sums = nums[:]
        for i in range(1, len(nums)):
            if sums[i - 1] + sums[i] > sums[i]:
                sums[i] = sums[i - 1] + sums[i]
                # backtrack[i] = True
            if sums[i] > max:
                max = sums[i]
                # max_i = i
        # end = max_i + 1
        # start = max_i
        # while backtrack[max_i]:
        #     max_i -= 1
        return max

ans = Solution()
print(ans.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
