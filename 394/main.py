"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        elif s[0].isdigit():
            encode_start = s.find('[')
            encode_end = find_matching(s[encode_start:]) + encode_start
            return int(s[:encode_start]) * self.decodeString(s[encode_start + 1: encode_end]) + self.decodeString(s[encode_end + 1:])
        else:
            return s[0] + self.decodeString(s[1:])

def find_matching(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '[':
            count += 1
        elif s[i] == ']':
            count -= 1
        if count == 0:
            return i



ans = Solution()
print(ans.decodeString("abcde"))
print(ans.decodeString("3[a]2[bc]"))
print(ans.decodeString("3[a2[c]]"))
print(ans.decodeString("2[abc]3[cd]ef"))