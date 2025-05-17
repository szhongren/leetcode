from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        approach
        count the frequencies
        then, from the largest number, iterate
        store max_frequency
        for each number, go down at most k, greedily add numbers
        return max
        state: freq | sorted_unique_nums | i | num | freq | remaining_k | curr_i
        [1,2,4], k = 5
        sorted: [4,2,1]
        f = 1
        r_k = 5
        n_i = 1
        smaller_num = 2
        diff=2
        m_i = 1
        r_k = 3
        f = 2
        """
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
        sorted_unique_numbers = list(sorted(frequencies.keys(), reverse=True))
        max_frequency = 0
        m = len(sorted_unique_numbers)
        for i, num in enumerate(sorted_unique_numbers):
            freq = frequencies[num]
            remaining_k = k
            for next_i in range(i + 1, m):
                smaller_number = sorted_unique_numbers[next_i]
                diff = num - smaller_number
                if remaining_k < diff:
                    break
                max_increments = min(remaining_k // diff, frequencies[smaller_number])
                remaining_k -= max_increments * diff
                while remaining_k < 0:
                    remaining_k += diff
                    max_increments -= 1
                freq += max_increments
            max_frequency = max(freq, max_frequency)
        return max_frequency

    def maxFrequency_model(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0  # sum of nums[left…right]
        ans = 1
        for right, x in enumerate(nums):
            total += x
            # cost to bring nums[left..right] all up to x is x*(window_size) - total
            while x * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans
