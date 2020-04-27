"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Credits:
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern):
            return False
        else:
            a2b = {}
            b2a = {}
            for (a, b) in zip(pattern, words):
                if a not in a2b and b not in b2a:
                    a2b[a] = b
                    b2a[b] = a
                elif a in a2b and a2b[a] != b:
                    return False
                elif b in b2a and b2a[b] != a:
                    return False
            return True

ans = Solution()
print(ans.wordPattern("abba", "dog cat cat dog"))