"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from random import randint

# class Heap(object):
#     def __init__(self, vals=[]):
#         self.values = vals
#         self.len = len(vals)
#         if self.len > 0:
#             self.heapify(self.parent(self.len - 1))

#     def __str__(self):
#         printed = 0
#         power = 1
#         res = ""
#         while printed < self.len:
#             res += str(self.values[printed: min(printed + power, self.len)]) + '\n'
#             printed += power
#             power <<= 1
#         return res

#     def parent(self, i):
#         if i == 0:
#             return 0
#         else:
#             return (i - 1) // 2

#     def leftChild(self, i):
#         if i * 2 + 1 < self.len:
#             return i * 2 + 1
#         else:
#             return None

#     def rightChild(self, i):
#         if i * 2 + 2 < self.len:
#             return i * 2 + 2
#         else:
#             return None

#     def siftdown(self, i):
#         curr_i = i
#         while self.leftChild(curr_i):
#             swap_i = curr_i

#             l_child_i = self.leftChild(curr_i)
#             if self.values[swap_i] < self.values[l_child_i]:
#                 swap_i = l_child_i

#             r_child_i = self.rightChild(curr_i)
#             if r_child_i and self.values[swap_i] < self.values[r_child_i]:
#                 swap_i = r_child_i

#             if swap_i == curr_i:
#                 return
#             else:
#                 self.values[curr_i], self.values[swap_i] = self.values[swap_i], self.values[curr_i]
#                 curr_i = swap_i

#     def heapify(self, start):
#         for i in range(start, -1, -1):
#             self.siftdown(i)

#     def pop(self):
#         if self.len == 0:
#             return None
#         self.values[0], self.values[self.len - 1] = self.values[self.len - 1], self.values[0]
#         self.len -= 1
#         self.heapify(self.parent(self.len - 1))
#         return self.values[self.len]

# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         counts = {}
#         for val in nums:
#             if val not in counts:
#                 counts[val] = 1
#             else:
#                 counts[val] += 1
#         count_to_val = [(counts[val], val) for val in counts]
#         h = Heap(count_to_val)
#         return [h.pop()[1] for _ in range(k)]

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

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        buckets = [{} for i in range(len(nums) + 1)]
        freq = {}
        for v in nums:
            if v not in freq:
                freq[v] = 1
                buckets[1][v] = True
            else:
                i = freq[v]
                del buckets[i][v]
                buckets[i + 1][v] = True
                freq[v] += 1
        ans = []
        i = len(nums)
        while len(ans) < k:
            for val in buckets[i]:
                ans.append(val)
            i -= 1
        return ans

ans = Solution()
# for _ in range(15):
#     values = [randint(-10, 10) for _ in range(randint(1, 30))]
#     print(values)
#     print(ans.topKFrequent(values, randint(1, len(set(values)))))
#     print()
print(ans.topKFrequent([4,1,-1,2,-1,2,3], 2))
print(ans.topKFrequent([1,1,1,2,2,3], 2))
