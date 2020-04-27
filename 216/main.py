"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        possible = [i + 1 for i in range(min(9, n - k + 1))]
        self.res = []
        self.combSumRecur(possible, k, n, [])
        return self.res

    def combSumRecur(self, possible, k, n, curr):
        if n == 0 and k == 0:
            self.res.append(curr)
        elif k == 0:
            return
        else:
            for i in range(len(possible)):
                val = possible[i]
                if val > n:
                    break
                else:
                    self.combSumRecur(possible[i + 1:], k - 1, n - val, curr + [val])




ans = Solution()
print(ans.combinationSum3(2, 18))
print(ans.combinationSum3(3, 9))