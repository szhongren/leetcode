from typing import List
from random import randint


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        target = randint(0, self.prefix_sums[-1] - 1)
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if target >= self.prefix_sums[mid]:  # Note: Changed > to >=
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
