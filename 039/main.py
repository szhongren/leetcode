"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.combinationSumRecur(sorted(candidates), target, 0, [])
        # self.res = list(map(sorted, self.res))
        # self.dedup = []
        # for s in self.res:
        #     if s not in self.dedup:
        #         self.dedup.append(s)
        return self.res

    def combinationSumRecur(self, candidates, target, start, curr_set):
        if target == 0:
            self.res.append(curr_set)
        else:
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                else:
                    self.combinationSumRecur(candidates, target - candidates[i], i, curr_set + [candidates[i]])
       # for each val in candidates, get target - val, then see if that is in candidates
        # if yes, add current set of vals to self.res
        # recur on target - val

ans = Solution()
print(ans.combinationSum([2, 3, 6, 7], 7))
print(ans.combinationSum([92,71,89,74,102,91,70,119,86,116,114,106,80,81,115,99,117,93,76,77,111,110,75,104,95,112,94,73], 310))