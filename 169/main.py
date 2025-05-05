from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        approach
        loop through list, count elements in a map, if any appears more than n // 2, return
        test cases:
        []
        [1]
        [1,1]
        [1,1,2]
        [1,2,2]
        """
        counts = {}
        threshold = len(nums) // 2
        for item in nums:
            if item not in counts:
                counts[item] = 0
            counts[item] += 1
            if counts[item] > threshold:
                return item
