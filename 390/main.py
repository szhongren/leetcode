"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return lastRemainingRecur(1, n, 1, True)

def lastRemainingRecur(start, end, step, forward):
    if start == end:
        return start
    else:
        l = (end - start) // step + 1 # gets the length of the sequence
        if forward:
            # alwaays starts at seq[1], and ends at seq[-1] if odd, seq[-2] if even
            return lastRemainingRecur(start + step, end - (l % 2) * step, step * 2, not forward)
        else:
            # always ends at seq[-1], and starts at seq[1] if odd, seq[0] if even
            return lastRemainingRecur(start + (l % 2) * step, end - step, step * 2, not forward)

ans = Solution()
for i in range(1,100):
    print(i, ans.lastRemaining(i))
    # print([x + 1 for x in range(i)])
"""
1 -> 1
2 -> 2
3 -> 2
4 -> 2
5 -> 2
6 -> 4
7 -> 4
8 -> 6
9 -> 6
10 -> 8
11 -> 8
12 -> 6
13 -> 6
14 -> 8
15 -> 8
16 -> 6
17 -> 6
18 -> 8
19 -> 8
20 -> 6
21 -> 6
2 4 6 8 10 12 14 16 18 20
2 6 10 14 18
6 14
"""