"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
class BinaryTrie(object):
    def __init__(self, bits, maxBits):
        if maxBits % bits != 0:
            raise ValueError('maxBits is not evenly divisible by bits')
            return
        self.isLeaf = False
        self.val = None
        self.keyBits = bits
        self.maxBits = maxBits
        self.children = {}

    def insert(self, val, end):
        if self.maxBits == 0:
            self.isLeaf = True
            self.val = end
            return
        firstBits = (val >> (self.maxBits - self.keyBits)) & (2 ** self.keyBits - 1)
        if firstBits not in self.children:
            self.children[firstBits] = BinaryTrie(self.keyBits, self.maxBits - self.keyBits)
        self.children[firstBits].insert(val, end)

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie = BinaryTrie(3, 6)
        for v in nums:
            trie.insert(v, v)
        pass

ans = Solution()
print(ans.findMaximumXOR([3, 10, 5, 25, 2, 8]))