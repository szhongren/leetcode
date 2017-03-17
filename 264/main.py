"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Hint:

    The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
    An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
    The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
    Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        numbers = {
            2: [1],
            3: [1],
            5: [1]
        }
        ans = None
        for i in range(n):
            vals = [numbers[i][0] for i in numbers]
            min_val = min(vals)
            for factor in numbers:
                numbers[factor].append(factor * min_val)
                if numbers[factor][0] == min_val:
                    numbers[factor] = numbers[factor][1:]
            ans = min_val
        return ans

ans = Solution()
for i in range(100):
    print(ans.nthUglyNumber(i))
