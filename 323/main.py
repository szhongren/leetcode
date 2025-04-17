from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Find number of connected components in an undirected graph using Union Find:
        1. Initialize each node as its own parent
        2. Process each edge by finding roots and joining components
        3. Count number of nodes that are their own parent (roots)
        """
        # Initialize each node to be its own parent
        parent_of = {k: k for k in range(n)}

        def find(x: int) -> int:
            # Path compression: recursively set each node's parent to root
            if parent_of[x] != x:
                parent_of[x] = find(parent_of[x])
            return parent_of[x]

        # Process each edge
        for edge in edges:
            a, b = edge[0], edge[1]

            # Find root of first node
            root_a = find(a)

            # Find root of second node
            root_b = find(b)

            # Union: join components if roots are different
            if root_a != root_b:
                parent_of[root_b] = root_a

        # Count roots (nodes that are their own parent)
        return len([k for k, v in parent_of.items() if k == v])


# Test cases
sol = Solution()
print(sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # Expected: 2 components
print(sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # Expected: 1 component
print(
    sol.countComponents(5, [[0, 1], [0, 2], [1, 2], [2, 3], [2, 4]])
)  # Expected: 1 component
