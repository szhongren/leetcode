class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        approach
        count number of chars with odd frequencies
        that's the minimum number of palindromes
        max is number of chars
        """
        freqs = {}
        for ch in s:
            if ch not in freqs:
                freqs[ch] = 0
            freqs[ch] += 1
        count_odd = 0
        for ch, count in freqs.items():
            if count % 2 == 1:
                count_odd += 1
        return count_odd <= k <= len(s)
