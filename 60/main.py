"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        facts = [1]
        for i in range(1, n):
            facts.append(i * facts[-1])
        # def getPermutationRecur(unused, i):
        #     l = len(unused)
        #     if l == 0:
        #         return ""
        #     first_digit = i // facts[l - 1]
        #     return unused[first_digit] + getPermutationRecur(unused[:first_digit] + unused[first_digit + 1:], i % facts[l - 1])
        # return getPermutationRecur([str(v + 1) for v in range(n)], k - 1)
        ans = ""
        unused = [str(v + 1) for v in range(n)]
        i = k - 1
        while n > 0:
            n -= 1
            ans += unused[i // facts[n]]
            unused.remove(ans[-1])
            i %= facts[n]
        return ans

ans = Solution()
for i in range(1, 7):
    print(ans.getPermutation(3, i))

for i in range(1, 25):
    print(ans.getPermutation(9, i))
