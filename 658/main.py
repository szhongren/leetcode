from typing import List
from heapq import heappush, heappop


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        approach
        use a max heap of (abs(diff), value), then sort by value
        pop from max heap when len(heap) > k
        """
        max_heap = []
        for value in arr:
            heappush(max_heap, (-abs(value - x), value))
            if len(max_heap) > k:
                heappop(max_heap)
        return sorted([x[1] for x in max_heap])
