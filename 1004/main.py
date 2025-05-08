from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        sliding window approach
        edge cases:
        []
        [0], k = 10
        [1,1,1,0,0,0,1,1,1,1,0]
        """
        n = len(nums)
        max_len = 0
        slow, fast = 0, 0
        used_flips = 0
        while fast < n:
            print(slow, fast, used_flips)
            max_len = max(max_len, fast - slow)
            digit = nums[fast]
            if digit == 1:
                fast += 1
            else:
                if used_flips < k:
                    used_flips += 1
                    fast += 1
                else:
                    if nums[slow] == 0:
                        used_flips -= 1
                    slow += 1
        return max(max_len, fast - slow)
