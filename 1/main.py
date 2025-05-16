from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        approach
        use a hashmap of value to index
        for every number, if target - num in seen:
        return index of that number, and index of current number
        """
        value_to_index = {}
        for i, num in enumerate(nums):
            if target - num in value_to_index:
                return [value_to_index[target - num], i]
            value_to_index[num] = i
