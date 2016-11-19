"""
takes 2 strings and returns the one in the second that was not in the first
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        final = 0
        for c in s:
            final = final ^ ord(c)
        for c in t:
            final = final ^ ord(c)
        return chr(final)

ans = Solution()
print(ans.findTheDifference("abcd", "abcde"))