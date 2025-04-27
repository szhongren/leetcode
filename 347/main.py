from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        approach
        count frequencies
        sort items by count
        print until we have all
        """
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        sorted_by_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        result = []
        for item in sorted_by_freq:
            if len(result) == k:
                break
            result.append(item[0])
        return result
