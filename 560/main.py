from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        sum_count = {0: 1}  # Initialize with 0 sum having count of 1

        for num in nums:
            # increment running sum
            curr_sum += num

            # If we've seen (curr_sum - k) before, it means we have subarrays summing to k
            if curr_sum - k in sum_count:
                # total count increments by number of previous sum subarrays
                # for example, if we see 5 on the previous, that means that there are 5 subarrays that add up to the previous, so we can add 5 to total because current sum - previous = k 5 ways
                count += sum_count[curr_sum - k]

            # Add current sum to our running counts
            sum_count[curr_sum] = sum_count.get(curr_sum, 0) + 1

        return count
