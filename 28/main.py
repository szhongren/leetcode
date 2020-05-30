"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(needle)
        l2 = len(haystack)
        if l1 > l2:
            return -1
        else:
            for i in range(l2 - l1 + 1):
                if needle == haystack[i:i + l1]:
                    return i
            return -1