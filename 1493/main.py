from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        approach: count number of subsequent 1s, and count of 0s in between
        if only 1 type:
        return 1s - 1
        return max(longest1s, a + b where a, b have 1 0 between)
        """
        counts = []
        current = nums[0]
        count = 0
        for x in nums:
            if x == current:
                count += 1
            else:
                counts.append((current, count))
                current = x
                count = 1
        counts.append((current, count))
        if len(counts) == 1:
            if counts[0][0] == 1:
                return counts[0][1] - 1
            else:
                return 0
        if len(counts) == 2:
            if counts[0][0] == 1:
                return counts[0][1]
            else:
                return counts[1][1]
        a, b = 0, 2
        max_1s = 0
        max_sum = 0
        while b < len(counts):
            first, last = counts[a], counts[b]
            if first[0] == 1:
                max_1s = max([max_1s, first[1], last[1]])
                max_sum = max(
                    max_sum, first[1] + last[1] if counts[a + 1][1] == 1 else 0
                )
            else:
                max_1s = max(max_1s, counts[a + 1][1])
            a += 1
            b += 1
        return max(max_1s, max_sum)


sol = Solution()
print(sol.longestSubarray([1, 1, 0, 1]))
print(sol.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(sol.longestSubarray([1, 1, 1]))
