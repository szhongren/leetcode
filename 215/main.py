from typing import List
from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        approach
        use min heap
        push every element
        if len(heap) > k:
        pop
        return heap[0]
        nlogn
        """
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]
