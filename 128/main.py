from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        union find with a twist
        eveny time we see a new number, union find with adjacent numbers that exist
        then, get their subsequence lengths and calculate the total subsequence lengths
        3 cases
        x has no neighbors
        -> create set
        -> set seq_length = 1
        x has 1 neighbor:
        -> union find
        -> set seq_length = neighbor + 1
        x has 2 neighbors:
        -> union find
        -> set seq_length = neighbor_a + neighbor_b + 1
        keep a running max
        """
        if len(nums) == 0:
            return 0
        self.result = 1
        parent_of = {x: x for x in nums}
        seq_length_of = {x: 1 for x in nums}

        def find_parent(node: int):
            if parent_of[node] == node:
                return node
            parent_of[node] = find_parent(parent_of[node])
            return parent_of[node]

        def union(a: int, b: int):
            parent_a, parent_b = find_parent(a), find_parent(b)
            if parent_a != parent_b:
                parent_of[parent_b] = parent_a
                seq_length_of[parent_a] = (
                    seq_length_of[parent_a] + seq_length_of[parent_b]
                )
                self.result = max(seq_length_of[parent_a], self.result)

        seen = set()
        for val in nums:
            if val - 1 in seen and val + 1 in seen:
                union(val - 1, val)
                union(val, val + 1)
            elif val - 1 in seen:
                union(val - 1, val)
            elif val + 1 in seen:
                union(val + 1, val)
            else:
                pass
            seen.add(val)
        return self.result
