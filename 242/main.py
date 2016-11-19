"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        found = {}
        for ch in s:
            if found.__contains__(ch):
                found[ch] += 1
            else:
                found[ch] = 1
        for ch in t:
            if found.__contains__(ch):
                if found[ch] > 0:
                    found[ch] -= 1
                else:
                    return False
            else:
                return False
        return True


ans = Solution()
print(ans.isAnagram("anagram", "nagaram"))
print(ans.isAnagram("rat", "car"))