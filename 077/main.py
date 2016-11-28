"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        else:
            res = []
            for i in range(1, n + 1):
                for item in self.combine(i - 1, k - 1):
                    res.append(item + [i])
            return res
        # faster solution somehow
        # if k == 0:
        #     return [[]]
        # return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]


ans = Solution()
print(ans.combine(4, 2))

"""
1 2 3
1 2 4
1 3 4
2 3 4
"""