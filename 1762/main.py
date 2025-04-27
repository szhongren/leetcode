from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        approach:
        have a max that represents tallest building to the right of this current location
        from -1 to 0, tallest_building_to_right = max(tallest, current), then if current < tallest_to_right, don't append to results list
        """
        max_height_to_right = 0
        result = []
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height_to_right:
                result.append(i)
            max_height_to_right = max(max_height_to_right, heights[i])
        return result[::-1]
