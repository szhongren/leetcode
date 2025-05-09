from typing import List
from heapq import heappush, heappop


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        approach
        use heap
        put everything into heap
        while heap[0] < k
            pop, pop
            push(min(x, y) * 2 + max(x, y))
        """
        heap = []
        for num in nums:
            heappush(heap, num)
        operations = 0
        while heap[0] < k:
            a, b = heappop(heap), heappop(heap)
            heappush(heap, min(a, b) * 2 + max(a, b))
            operations += 1
        return operations
