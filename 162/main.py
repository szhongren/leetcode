from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        divide and conquer
        """

        def findPeakElementRecur(i: int, j: int) -> int:
            mid = (i + j) // 2
            if i == j:
                return i
            if nums[mid] > nums[mid + 1]:
                return findPeakElementRecur(i, mid)
            return findPeakElementRecur(mid + 1, j)
            # look to both sides

        return findPeakElementRecur(0, len(nums) - 1)
