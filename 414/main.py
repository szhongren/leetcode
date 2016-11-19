# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).
import math

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = [-math.inf, -math.inf, -math.inf]
        seen = {}
        for i in nums:
            if seen.__contains__(i):
                continue
            if i > max[0]:
                max[2] = max[1]
                max[1] = max[0]
                max[0] = i
            elif i > max[1]:
                max[2] = max[1]
                max[1] = i
            elif i > max[2]:
                max[2] = i
            seen[i] = True

        if max[2] == -math.inf:
            return max[0]
        else:
            return max[2]


ans = Solution()
print(ans.thirdMax([2, 2, 3, 1]))