from typing import List
from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        """
        approach:
        use min heap to push sums onto the min heap
        """
        a, b = nums1[0], nums2[0]
        seen = set([(0, 0)])
        heap = [(a + b, 0, 0)]
        result = []
        while len(result) < k:
            _, x, y = heappop(heap)
            if x + 1 < len(nums1) and y < len(nums2) and (x + 1, y) not in seen:
                heappush(heap, (nums1[x + 1] + nums2[y], x + 1, y))
            seen.add((x + 1, y))
            if x < len(nums1) and y + 1 < len(nums2) and (x, y + 1) not in seen:
                heappush(heap, (nums1[x] + nums2[y + 1], x, y + 1))
            seen.add((x, y + 1))
            result.append([nums1[x], nums2[y]])
        return result


sol = Solution()
print(sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
