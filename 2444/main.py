from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        """
        approach
        for every position, set this as end
        look back with another slow pointer incrementing until
        if nums[0] between min and max
            increment fast
        """
        pass
