class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        approach
        go through the strings, and check ifd there are only 2 different chars
        """
        m = len(s1)
        n = len(s2)
        if m != n:
            return False
        count_diff = 0
        diff_i = []
        for i in range(m):
            if s1[i] != s2[i]:
                count_diff += 1
                diff_i.append(i)
            if count_diff > 2:
                return False
        if count_diff == 0:
            return True
        if count_diff == 2:
            i1, i2 = diff_i[0], diff_i[1]
            return s1[i1] == s2[i2] and s1[i2] == s2[i1]
        return False
