from typing import List
from math import inf


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        approach
        use sliding window, works because it's all positive
        keep a min len, and return at the end
        edge cases:
        [] -> not possible
        [1], 1
        [1, 1], 3
        """
        slow, fast = 0, 0
        running_sum = nums[0]
        n = len(nums)
        nums.append(0)
        max_len = inf
        while fast < n and slow <= fast:
            if running_sum < target:
                fast += 1
                running_sum += nums[fast]
            else:
                max_len = min(max_len, fast - slow + 1)
                running_sum -= nums[slow]
                slow += 1
        if max_len == inf:
            return 0
        return max_len
