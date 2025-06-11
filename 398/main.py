from typing import List
from random import randint


class Solution:
    """
    approach
    preprocess, for each number, save a map of the indices
    """

    def __init__(self, nums: List[int]):
        self.number_to_indices = {}
        for i, num in enumerate(nums):
            if num not in self.number_to_indices:
                self.number_to_indices[num] = []
            self.number_to_indices[num].append(i)

    def pick(self, target: int) -> int:
        if target not in self.number_to_indices:
            return None
        n = len(self.number_to_indices[target])
        index = randint(0, n - 1)
        return self.number_to_indices[target][index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
