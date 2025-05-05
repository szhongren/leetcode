class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        approach
        2 pointers
        if a == b
        advance both
        """
        a, b = 0, 0
        while True:
            if a == len(s):
                return True
            elif b == len(t):
                return False
            ch_a, ch_b = s[a], t[b]
            if ch_a == ch_b:
                a += 1
                b += 1
            else:
                b += 1
