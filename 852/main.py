from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        approach
        binary search
        look at midpoint, and figure out the slope
        3 cases
        low to high
        high to low
        peak in middle
        edge cases:
        0, 1, 2 elements
        [0, 1, 2, -1]
        0, 2
        m = 1
        a = 0, b = 1, c = 2
        2, 2
        [2, 1, 0]
        0, 2
        m = 1
        a = 2, b = 1, c = 0
        end = 0
        [0, 1, 0]
        """
        n = len(arr)
        arr.append(-1)

        start, end = 0, n - 1
        while start < end:
            midpoint = (start + end) // 2
            a, b, c = arr[midpoint - 1], arr[midpoint], arr[midpoint + 1]
            if a > b:
                end = midpoint - 1
            elif b < c:
                start = midpoint + 1
            else:
                return midpoint
        return start
