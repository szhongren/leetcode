from typing import List
from heapq import heappop, heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        approach
        use a heap
        iterate through the matrix
        if len(heap) > k
        pop
        """
        heap = []
        for row in matrix:
            for cell in row:
                heappush(heap, -cell)
                if len(heap) > k:
                    heappop(heap)
        return -heap[0]
