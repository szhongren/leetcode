"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

def arrange_cmp(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # sort into buckets by first char, then sort each by the remaining chars, with the one with fewest chars in the middle instoad of the front
        return sorted(list(map(str, nums)), cmp = arrange_cmp)

ans = Solution()
print(ans.largestNumber([3, 30, 34, 5, 9]))
