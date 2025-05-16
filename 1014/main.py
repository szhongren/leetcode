from typing import List
from math import inf


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        do same as stock sales
        track max(values[i] + i)
        and max_score
        """
        highest_prev_spot = -inf
        max_score = 0
        for i, score in enumerate(values):
            if max_score < highest_prev_spot + score - i:
                max_score = highest_prev_spot + score - i
            if score + i > highest_prev_spot:
                highest_prev_spot = score + i
        return max_score
