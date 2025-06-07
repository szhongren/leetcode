from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        """
        approach
        2 pointers/sliding window
        count number of subarrays that end at i, and add to accumulator
        """
        total = 0
        n = len(nums)
        max_value = max(nums)
        start = 0
        count_of_max = 0
        for i in range(n):
            if nums[i] == max_value:
                count_of_max += 1
            if count_of_max < k:
                continue
            elif count_of_max == k:
                while nums[start] != max_value:
                    start += 1
            elif count_of_max > k:
                while count_of_max > k:
                    if nums[start] == max_value:
                        count_of_max -= 1
                    start += 1
                while nums[start] != max_value:
                    start += 1
            total += start + 1
        return total
