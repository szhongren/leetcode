# longest palindromic substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        chars = []
        for (c, mark) in zip(list(s), (['#'] * length)):
            chars.append(mark)
            chars.append(c)
        chars.append('#')
        lengths = [i % 2 for i in range(len(s) * 2 + 1)]
        for i in range(len(chars)):

def ifPalindrome(s, mid, ):



ans = Solution()
print(ans.longestPalindrome("character"))