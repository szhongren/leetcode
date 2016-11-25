"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        most_freq = []
        counts = {}
        in_list = {}
        curr_i = 0
        for v in nums:
            if v in counts:
                counts[v] += 1
                if v in in_list:
                    if in_list[v] != 0:
                        if counts[v] > counts[most_freq[in_list[v] - 1]]:
                            most_freq[in_list[v]], most_freq[in_list[v] - 1] = most_freq[in_list[v] - 1], most_freq[in_list[v]]
                            in_list[most_freq[in_list[v]]] += 1
                            in_list[v] -= 1
                else:
                    if counts[v] > counts[most_freq[-1]]:
                        del in_list[most_freq[-1]]
                        curr_i -= 1
                        most_freq = most_freq[:-1]
                        in_list[v] = curr_i
                        curr_i += 1
                        most_freq.append(v)
            else:
                if curr_i != k:
                    in_list[v] = curr_i
                    curr_i += 1
                    most_freq.append(v)
                counts[v] = 1

        return most_freq

ans = Solution()
print(ans.topKFrequent([4,1,-1,2,-1,2,3], 2))
print(ans.topKFrequent([1,1,1,2,2,3], 2))