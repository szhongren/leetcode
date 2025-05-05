from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        reverse, then reverse first k, and reverse rest
        """
        n = len(nums)

        def reverse(start: int, end: int):
            if start >= end:
                return
            nums[start], nums[end] = nums[end], nums[start]
            reverse(start + 1, end - 1)

        reverse(0, n - 1)
        reverse(0, (k % n) - 1)
        reverse(k % n, n - 1)
