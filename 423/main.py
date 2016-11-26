"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"
"""

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = {}
        counts['z'] = 0
        counts['w'] = 0
        counts['u'] = 0
        counts['x'] = 0
        counts['g'] = 0
        counts['h'] = 0
        counts['f'] = 0
        counts['v'] = 0
        counts['i'] = 0
        counts['o'] = 0

        for ch in s:
            if ch in counts:
                counts[ch] += 1

        res = ""
        res += '0' * counts['z']
        res += '1' * (counts['o'] - counts['w'] - counts['z'] - counts['u'])
        res += '2' * counts['w']
        res += '3' * (counts['h'] - counts['g'])
        res += '4' * counts['u']
        res += '5' * (counts['f'] - counts['u'])
        res += '6' * counts['x']
        res += '7' * (counts['v'] - counts['f'] + counts['u'])
        res += '8' * counts['g']
        res += '9' * (counts['i'] - counts['f'] + counts['u'] - counts['g'] - counts['x'])

        return res

"""
zero - z
two - w
four - u
six - x
eight - g

three - h-g
five - f-u
seven - v-f+u
nine - i-f+u-g-x
one - o-w-z-u
"""


ans = Solution()
print(ans.originalDigits("owoztneoer"))
print(ans.originalDigits("fviefuro"))