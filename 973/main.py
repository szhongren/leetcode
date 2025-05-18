from typing import List
from heapq import heappop, heappush


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        approach
        for every point, put into heap (sqrt(x1 **2 - x2 ** 2) + (y1 ** 2 - y2 ** 2))
        if heap size > k, pop
        """
        heap = []
        for x, y in points:
            dist = pow(x**2 + y**2, 0.5)
            heappush(heap, (-dist, (x, y)))
            if len(heap) > k:
                heappop(heap)
        return [xy for _, xy in heap]
