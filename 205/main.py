"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        shifts = {}
        t_seen = {}
        for (a, b) in zip(s, t):
            if shifts.__contains__(a):
                if b != chr(ord(a) + shifts[a]):
                    return False
            elif b not in t_seen:
                shifts[a] = ord(b) - ord(a)
                t_seen[b] = True
            else:
                return False
        return True

ans = Solution()
print(ans.isIsomorphic("ab", "aa"))
print(ans.isIsomorphic("foo", "bar"))
print(ans.isIsomorphic("egg", "add"))
print(ans.isIsomorphic("paper", "title"))