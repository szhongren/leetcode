"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for ch in s:
            if counts.__contains__(ch):
                counts[ch] += 1
            else:
                counts[ch] = 1
        potential = []
        for (ch, v) in counts.items():
            if v == 1:
                potential.append(ch)

        if len(potential) == 0:
            return -1
        for i in range(len(s)):
            if s[i] in potential:
                return i


ans = Solution()
print(ans.firstUniqChar("leetcode"))
print(ans.firstUniqChar("cc"))
print(ans.firstUniqChar("loveleetcode"))