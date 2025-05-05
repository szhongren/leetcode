from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0:
            return 0

        # Create counts array (needs to be size n+1 for counting sort)
        counts = [0] * (n + 1)

        # Count papers with at least i citations
        for val in citations:
            counts[min(val, n)] += 1

        # Check from highest possible h-index down
        papers = 0
        for i in range(n, -1, -1):
            papers += counts[i]
            if papers >= i:
                return i

        return 0


"""
edge cases
[]
[1]
[2]
[1,1]
"""
