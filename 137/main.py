"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        results = []
        for v in nums:
            if seen.__contains__(v) == False:
                seen[v] = 1
                results.append(v)
            else:
                seen[v] += 1
                if seen[v] == 2:
                    results.remove(v)
        return results[0]

ans = Solution()
print(ans.singleNumber([1, 2, 1, 1]))
print(ans.singleNumber([1, 2, 1, 1, 9, 9, 9]))
print(ans.singleNumber([1, 2, 1, 9, 4, 2, 1, 2, 9, 9]))