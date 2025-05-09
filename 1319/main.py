from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        approach
        for n computers, we need n-1 cables in a min spanning tree
        so, we can check that first, if there's fewer than n-1 cables, return false
        else, do union find
        that will give us the number of disconnected groups
        that m - 1 will give us the number of cables we need to move
        """
        num_connections = len(connections)
        if num_connections < n - 1:
            return -1

        parent_of = [n for n in range(n)]

        def find_parent(n: int):
            if parent_of[n] == n:
                return n
            parent_of[n] = find_parent(parent_of[n])
            return parent_of[n]

        def union(a: int, b: int):
            parent_a, parent_b = find_parent(a), find_parent(b)
            if parent_a == parent_b:
                return
            parent_of[parent_b] = parent_a

        for connection in connections:
            a, b = connection[0], connection[1]
            union(a, b)

        unique_parents = set()
        for i in range(n):
            unique_parents.add(find_parent(i))
        return len(unique_parents) - 1
