from typing import List


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def get_parent(a: int):
            if parents[a] == a:
                return a
            parents[a] = get_parent(parents[a])
            return parents[a]

        def union(a: int, b: int):
            parent_a, parent_b = get_parent(a), get_parent(b)
            if parent_a != parent_b:
                parents[parent_b] = parent_a
                return True
            return False

        sorted_connections = sorted(connections, key=lambda x: x[2])
        total_cost = 0
        edges_used = 0

        for a, b, cost in sorted_connections:
            if union(a - 1, b - 1):  # Convert to 0-based indexing
                total_cost += cost
                edges_used += 1

        # Check if all nodes are connected
        if edges_used == n - 1:
            return total_cost
        return -1
