from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        approach
        2 pointers
        at each pair, move the smaller one, as that is the only way in which the total water may increase
        """
        n = len(height)
        start, end = 0, n - 1
        max_water = 0
        while start < end:
            a, b = height[start], height[end]
            max_water = max(max_water, (end - start) * min(a, b))
            if a < b:
                start += 1
            else:
                end -= 1
        return max_water
