"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.combinationSum2Recur(sorted(candidates), target, 0, [])
        self.dedup = []
        for res in self.res:
            if res not in self.dedup:
                self.dedup.append(res)
        return self.dedup

    def combinationSum2Recur(self, candidates, target, start, curr_set):
        if target == 0:
            self.res.append(curr_set)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                else:
                    self.combinationSum2Recur(candidates, target - candidates[i], i + 1, curr_set + [candidates[i]])

ans = Solution()
print(ans.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))