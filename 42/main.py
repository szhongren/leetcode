from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        approach
        preprocess the heights
        from left, for each spot, get the highest point to the left
        from right, for each spot, get the highest point to the right
        """
        peak_to_left = []
        max_height = 0
        for i in range(len(height)):
            peak_to_left.append(max_height)
            max_height = max(max_height, height[i])
        peak_to_right = []
        max_height = 0
        for i in range(len(height) - 1, -1, -1):
            peak_to_right.append(max_height)
            max_height = max(max_height, height[i])
        peak_to_right.reverse()
        total_water_trapped = 0
        for i in range(len(height)):
            water_trapped_here = min(peak_to_left[i], peak_to_right[i]) - height[i]
            if water_trapped_here > 0:
                total_water_trapped += water_trapped_here
        return total_water_trapped
