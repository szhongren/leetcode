"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))

ans = Solution()
for i in range(1, 5):
    print(i, ans.convertToTitle(i))
for i in range(24, 30):
    print(i, ans.convertToTitle(i))
for i in range(26*26 - 3, 26*26 + 4):
    print(i, ans.convertToTitle(i))