"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [1]
        while len(ans) < n:
            next_v = ans[-1] * 10
            while next_v > n:
                next_v //= 10
                next_v += 1
                while next_v % 10 == 0:
                    next_v //= 10
            ans.append(next_v)
        return ans

ans = Solution()
for i in range(1, 42):
    print(i, ans.lexicalOrder(i))
