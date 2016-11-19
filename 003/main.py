"""
Given a string, find the length of the longest substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # s_mod = "_" + s
        found = {}
        max_len = 0
        curr_len = 0
        trailing = -1
        for i in range(len(s)):
            curr_char = s[i]
            if curr_char in found and found[curr_char] > trailing:
                trailing = found[curr_char]
                curr_len = i - trailing
            else:
                curr_len += 1
                if curr_len > max_len:
                    max_len = curr_len
            found[curr_char] = i
        return max_len

ans = Solution()
print(ans.lengthOfLongestSubstring("aab"))
print(ans.lengthOfLongestSubstring("pwwkew"))
print(ans.lengthOfLongestSubstring("tmmzuxt"))

