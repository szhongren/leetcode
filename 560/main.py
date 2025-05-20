from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        approach
        have a count, and a running sum
        for every element, add to the running sum
        if I see sum-k before, that means there are subarrays that sum to k (ie from i to previous i)
        set sum count += 1
        o(n), iterate through list 1 time
        """
        count = 0
        acc = 0
        sums_count = {0: 1}
        for num in nums:
            acc += num
            if acc - k in sums_count:
                count += sums_count[acc - k]
            sums_count[acc] = sums_count.get(acc, 0) + 1
        return count
