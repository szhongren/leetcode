"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        add = 1
        curr_sq = 0
        while curr_sq <= num:
            if curr_sq == num:
                return True
            else:
                curr_sq += add
                add += 2
        return False