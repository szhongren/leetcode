"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        added = 9
        num_digits = 1
        total = 0
        end = 1
        while total < n:
            total += num_digits * added
            num_digits += 1
            added *= 10
            end *= 10
        num_digits -= 1
        added /= 10
        curr = str(end - 1 - (total - n) // num_digits)
        prev = n - (total - num_digits * added)
        digit_i = int(prev % num_digits)
        if digit_i == 0:
            return int(curr[-1])
        else:
            return int(curr[digit_i - 1])

ans = Solution()
for i in range(1, 30):
    print(i, ans.findNthDigit(i))
for i in range(187, 195):
    print(i, ans.findNthDigit(i))
