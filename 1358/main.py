class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        approach
        brute force, for every index, expand until we have at least 3, then we can add all the rest
        """
        n = len(s)
        if n < 3:
            return 0
        result = 0
        for i in range(n - 2):
            to_find = set(["a", "b", "c"])
            for j in range(i, n):
                if s[j] in to_find:
                    to_find.remove(s[j])
                if len(to_find) == 0:
                    break
            if len(to_find) == 0:
                result += n - j
        return result

    def numberOfSubstrings_model(self, s: str) -> int:
        # Track last position of a, b, c
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            # Update last position of current character
            last_pos[ord(s[pos]) - ord("a")] = pos

            # Add count of valid substrings ending at current position
            # If any character is missing, min will be -1
            # Else min gives leftmost required character position
            total += 1 + min(last_pos)

        return total
