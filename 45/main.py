from typing import List
from math import inf
from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        bfs
        recursive or loop
        """
        n = len(nums)
        min_jumps = [inf] * n
        min_jumps[0] = 0
        queue = deque([0])
        while queue:
            curr = queue.popleft()
            if curr == n - 1:
                return min_jumps[curr]
            for target in range(curr + 1, min(n, curr + nums[curr] + 1)):
                if min_jumps[target] != inf:
                    continue
                min_jumps[target] = min(min_jumps[target], min_jumps[curr] + 1)
                queue.append(target)


"""
edge cases
[] -> not possible
[1] -> 0
[1, 0] -> 1
"""
