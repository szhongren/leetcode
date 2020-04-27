"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_vals = [str(v) for v in nums]
        max_l = max(map(len, str_vals))
        # get ready to sort the thing, using the key that is just the str repeated
        tmp = [((v * max_l)[:max_l + 1], v) for v in str_vals]
        # tmp = list(map(lambda x: (x, (x * max_l)[:max_l + 1]), str_vals))
        final = ''.join([v[1] for v in sorted(tmp, reverse=True)])
        return final[:-1].lstrip('0') + final[-1]

ans = Solution()
print(ans.largestNumber([3, 30, 34, 5, 9]))
print(ans.largestNumber([2,10]))
print(ans.largestNumber([12,121]))
print(ans.largestNumber([0,0]))
print(ans.largestNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))
