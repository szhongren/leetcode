from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        approach
        find sequences of 0s, add to a list
        then, process the list
        for 1 0, +1 to count
        for 2 0s, + n + (n - 1)
        for 3 0s, + n + (n - 1) + (n - 2)
        + 1 * 1
        + 2 * 1 + 1 * 2
        + 3 * 1 + 2 * 2 + 1 * 3
        """
        sequence_lengths = []
        current_sequence_length = 0
        for val in nums:
            if val != 0:
                if current_sequence_length != 0:
                    sequence_lengths.append(current_sequence_length)
                current_sequence_length = 0
            else:
                current_sequence_length += 1
        if current_sequence_length != 0:
            sequence_lengths.append(current_sequence_length)
        result = 0
        for l in sequence_lengths:
            for i in range(l):
                result += l - i
        return result
