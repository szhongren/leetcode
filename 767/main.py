class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        approach
        we don't need to simulate the thing, we can work with just the counts
        crucially, if len(s) is even, then return true if no char has count > half
        if len(s) is odd, then return true if no char has count > half rounded up
        """
        n = len(s)
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = 0
            counts[ch] += 1
            if n % 2 == 0:
                if counts[ch] > n / 2:
                    return ""
            else:
                if counts[ch] > n // 2 + 1:
                    return ""

        reverse_map = {v: [] for v in counts.values()}
        for ch, count in counts.items():
            reverse_map[count].append(ch)

        chars = ""
        for count in sorted(reverse_map.keys(), reverse=True):
            for ch in reverse_map[count]:
                for _ in range(count):
                    chars += ch

        positions = list(range(0, n, 2)) + list(range(1, n, 2))
        chars_and_pos = sorted(zip(positions, chars))
        result = ""
        for _, ch in chars_and_pos:
            result += ch
        return result


sol = Solution()
sol.reorganizeString("aab")
