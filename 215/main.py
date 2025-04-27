from typing import List
from heapq import heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        approach:
        use a min heap, every time it goes over size k, drop the minimum number
        """
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]
