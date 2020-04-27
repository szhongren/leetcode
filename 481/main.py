"""
A magical string S consists of only '1' and '2' and obeys the following rules:

The string S is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string S itself.

The first few elements of string S is the following: S = "1221121221221121122……"

If we group the consecutive '1's and '2's in S, it will be:

1 22 11 2 1 22 1 22 11 2 11 22 ......

and the occurrences of '1's or '2's in each group are:

1 2 2 1 1 2 1 2 2 1 2 2 ......

You can see that the occurrence sequence above is the S itself.

Given an integer N as input, return the number of '1's in the first N number in the magical string S.

Note: N will not exceed 100,000.

Example 1:

Input: 6
Output: 3
Explanation: The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
"""

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.mapping = {"1": {"1": "2", "2": "1"}, "2": {"1": "22", "2": "11"}}
        self.count = 1
        self.genString("122", "11", n)
        return self.count

    def genString(self, curr, add, n):
        if n <= 3:
            if n == 0:
                self.count = 0
            return "122"[:n]
        else:
            new_curr = curr + add
            new_add = add[-1]
            for i, digit in enumerate(add):
                if digit == "1" and len(curr) + i + 1 <= n:
                    self.count += 1
                new_add += self.mapping[digit][new_add[-1]]
            if len(curr) > n:
                return curr[:n]
            return self.genString(new_curr, new_add[1:], n)

ans = Solution()
for i in range(1000):
    print(i, ans.magicalString(i))
