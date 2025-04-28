from typing import List, Set


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        """
        Using Bellman-Ford to find maximum probability path
        Note: We use multiplication for probabilities instead of addition for distances
        """
        # Initialize probabilities
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0

        # Relax edges n-1 times
        for _ in range(n - 1):
            updated = False
            # Try all edges
            for (u, v), prob in zip(edges, succProb):
                # Update probability if we find a better path
                # Check both directions since graph is undirected
                if probabilities[u] * prob > probabilities[v]:
                    probabilities[v] = probabilities[u] * prob
                    updated = True
                if probabilities[v] * prob > probabilities[u]:
                    probabilities[u] = probabilities[v] * prob
                    updated = True

            # Early stopping if no updates were made
            if not updated:
                break

        return probabilities[end_node]
