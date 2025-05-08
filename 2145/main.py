from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        """
        approach
        find difference between lowest and highest value, start from zero, keep track of min and max
        shift
        diff is (upper - lower) - diff

        edge cases:
        upper - lower < diff -> clamp to 0
        """
        min_val = 0
        max_val = 0
        acc = 0
        for diff in differences:
            acc += diff
            min_val = min(min_val, acc)
            max_val = max(max_val, acc)

        actual_range = max_val - min_val
        return max((upper + 1 - lower) - actual_range, 0)
