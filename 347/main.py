"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from random import randint

class Heap(object):
    def __init__(self, vals=[]):
        self.values = vals
        self.len = len(vals)

    def __str__(self):
        printed = 0
        power = 1
        res = ""
        while printed < self.len:
            res += str(self.values[printed: printed + power]) + '\n'
            printed += power
            power <<= 1
        return res

    def parent(self, i):
        if i == 0:
            return 0
        else:
            return (i - 1) // 2

    def leftChild(self, i):
        if i * 2 + 1 < self.len:
            return i * 2 + 1
        else:
            return None

    def rightChild(self, i):
        if i * 2 + 2 < self.len:
            return i * 2 + 2
        else:
            return None

    def siftdown(self, i):
        curr_i = i
        while self.leftChild(curr_i):
            child = self.leftChild(curr_i)
            swap_i = curr_i

            if self.values[swap_i] < self.values[child]:
                swap_i = child
            if self.rightChild(curr_i) and self.values[swap_i] < self.values[self.rightChild(curr_i)]:
                swap_i = self.rightChild(curr_i)
            if swap_i == curr_i:
                return
            else:
                self.values[curr_i], self.values[swap_i] = self.values[swap_i], self.values[curr_i]
                curr_i = swap_i

    def heapify(self, start):
        for i in range(start, -1, -1):
            self.siftdown(i)
        return

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for val in nums:
            if val not in counts:
                counts[val] = 1
            else:
                counts[val] += 1
        h = Heap(nums)
        print(nums, len(nums))
        h.heapify(h.parent(h.len - 1))
        return h

        # most_freq = []
        # counts = {}
        # in_list = {}
        # curr_i = 0
        # for v in nums:
        #     if v in counts:
        #         counts[v] += 1
        #         if v in in_list:
        #             if in_list[v] != 0:
        #                 if counts[v] > counts[most_freq[in_list[v] - 1]]:
        #                     most_freq[in_list[v]], most_freq[in_list[v] - 1] = most_freq[in_list[v] - 1], most_freq[in_list[v]]
        #                     in_list[most_freq[in_list[v]]] += 1
        #                     in_list[v] -= 1
        #         else:
        #             if counts[v] > counts[most_freq[-1]]:
        #                 del in_list[most_freq[-1]]
        #                 curr_i -= 1
        #                 most_freq = most_freq[:-1]
        #                 in_list[v] = curr_i
        #                 curr_i += 1
        #                 most_freq.append(v)
        #     else:
        #         if curr_i != k:
        #             in_list[v] = curr_i
        #             curr_i += 1
        #             most_freq.append(v)
        #         counts[v] = 1

        # return most_freq

ans = Solution()
for _ in range(15):
    values = [randint(-10, 10) for _ in range(randint(1, 30))]
    print(ans.topKFrequent(values, 2))
print(ans.topKFrequent([4,1,-1,2,-1,2,3], 2))
print(ans.topKFrequent([1,1,1,2,2,3], 2))
