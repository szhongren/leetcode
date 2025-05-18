from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        approach
        from the right, keep track of the tallest building
        if tallest to right >= current building, push i onto stack
        return stack.reverse
        edge cases:
        0 -> not possible
        1 -> return [0]
        O(n)
        """
        tallest_to_right = 0
        n = len(heights)
        result = []
        for i in range(n - 1, -1, -1):
            if heights[i] > tallest_to_right:
                result.append(i)
            tallest_to_right = max(tallest_to_right, heights[i])
        return list(reversed(result))
