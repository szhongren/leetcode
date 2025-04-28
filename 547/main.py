from typing import List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        approach:
        BFS through each unvisited city
        Count number of distinct connected components
        """
        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                queue = deque([city])

                while queue:
                    current = queue.popleft()
                    visited.add(current)

                    for neighbor in range(n):
                        if (
                            isConnected[current][neighbor] == 1
                            and neighbor not in visited
                        ):
                            queue.append(neighbor)

        return provinces
