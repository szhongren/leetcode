"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        counts = {}
        for v in nums:
            if v in counts:
                counts[v] += 1
            else:
                counts[v] = 1
        ans = []
        seen = {0}
        for v in counts.keys():
            counts[v] -= 1
            for w in counts.keys():
                if counts[w] == 0:
                    continue
                counts[w] -= 1
                for x in counts.keys():
                    if counts[x] == 0:
                        continue
                    counts[x] -= 1
                    curr = target - v - w - x
                    if curr not in counts:
                        counts[x] += 1
                        continue
                    quadlet = sorted([v, w, x, curr])
                    sig = tuple(quadlet)
                    if counts[curr] > 0 and sig not in seen:
                        ans.append(quadlet)
                        seen.add(sig)
                    counts[x] += 1
                counts[w] += 1
            counts[v] += 1
        return ans

ans = Solution()
print(ans.fourSum([1, 0, -1, 0, -2, 2], 0))
