class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        approach
        2 maps, forward and backward
        edge cases:
        different lens -> impossible
        """
        forward = {}
        backward = {}
        for i in range(len(s)):
            a, b = s[i], t[i]
            if a not in forward and b not in backward:
                forward[a] = b
                backward[b] = a
            if a in forward:
                if forward[a] != b:
                    return False
            if b in backward:
                if backward[b] != a:
                    return False
        return True
