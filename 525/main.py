from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        approach
        if 1, +1, else -1
        then, where count[i] + count[j] == 0 is a valid subarray
        ---
        [0]
        [0, -1]
        i=0,j=1
        return 0
        ---
        [0, 1]
        [0, -1, 0]
        i=0,j=2
        max=2
        i=1,j=2
        return 2
        ---
        [0, 0]
        [0, -1, -2]
        ---
        [0, 1, 1, 1, 1, 1, 0, 0, 0]
        [0, -1, 0, 1, 2, 3, 4, 3, 2, 1]
        i=0,j=9
        i=0,j=2
        max=2
        i=1
        i=2
        i=3,j=9
        """
        first_seen_counts = {0: -1}
        count = 0
        max_len = 0
        for i, num in enumerate(nums):  # O(n)
            if num == 1:
                count += 1
            else:
                count -= 1
            if count not in first_seen_counts:
                first_seen_counts[count] = i
            else:
                max_len = max(max_len, i - first_seen_counts[count])
        return max_len
