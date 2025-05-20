from typing import List
from random import randint


"""
approach
sum weights to get the random number 
use binary search to find the number it's representing, by keeping a prefix sum array, then we can just find the last prefix sum that's smaller than the random number
"""


class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.prefix_sums = []
        acc = 0
        for val in w:
            acc += val
            self.prefix_sums.append(acc)

    def pickIndex(self) -> int:
        pick = randint(1, self.prefix_sums[-1])
        low, high = 0, self.n
        while low < high:
            midpoint = (low + high) // 2
            if self.prefix_sums[midpoint] >= pick:
                high = midpoint
            else:
                low = midpoint + 1
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

sol = Solution([1, 3])
print(sol.prefix_sums)
