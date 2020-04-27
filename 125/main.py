"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0
        back = len(s) - 1
        while front <= back:
            f = s[front]
            b = s[back]
            if not f.isalnum():
                front += 1
                continue
            elif not b.isalnum():
                back -= 1
                continue
            else:
                f = f.lower()
                b = b.lower()
                if f != b:
                    return False
                front += 1
                back -= 1
        return True

ans = Solution()
print(ans.isPalindrome("A man, a plan, a canal: Panama"))
print(ans.isPalindrome("race a car"))