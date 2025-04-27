from typing import List
from heapq import heappush, heappop
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist_to_coord = {}
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            if dist not in dist_to_coord:
                dist_to_coord[dist] = []
            dist_to_coord[dist].append([x, y])
            heappush(heap, dist)
        result = []
        while len(result) < k:
            dist = heappop(heap)
            result += dist_to_coord[dist]
        return result[:k]
