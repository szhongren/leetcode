"""
Given an integer, write a function to determine if it is a power of two.
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        found_bit = False
        while n != 0:
            if n & 0x1 == 1:
                if found_bit:
                    return False
                else:
                    found_bit = True
            n >>= 1

        if found_bit:
            return True
        else:
            return False

ans = Solution()
print(ans.isPowerOfTwo(2))
print(ans.isPowerOfTwo(1))
print(ans.isPowerOfTwo(0))
print(ans.isPowerOfTwo(3))