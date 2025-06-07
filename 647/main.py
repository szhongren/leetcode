class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        approach
        for each 1 ch, spread out and +1 if still palindrome
        for each 2 ch, spread out and +1 if still palindrome
        """
        total = 0
        n = len(s)
        for i in range(n):
            front, back = i, i
            while front >= 0 and back < n:
                if s[front] != s[back]:
                    break
                total += 1
                front -= 1
                back += 1
        for i in range(n - 1):
            front, back = i, i + 1
            while front >= 0 and back < n:
                if s[front] != s[back]:
                    break
                total += 1
                front -= 1
                back += 1
        return total
