from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        """
        total_counts = {}
        for list in responses
            seen = {}
            for response in list:
                if response not in seen:
                    total_counts[word] += 1
                seen.add(response)
        sort by frequencies, then word
        return first
        """
        total_counts = {}
        for ls in responses:
            seen = set()
            for response in ls:
                if response not in seen:
                    if response not in total_counts:
                        total_counts[response] = 0
                    total_counts[response] += 1
                seen.add(response)

        return sorted(total_counts.items(), key=lambda x: (x[1], x[0]))[-1][0]
