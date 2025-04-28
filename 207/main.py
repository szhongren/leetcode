from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        approach
        do topo sort on courses
        return if topo sort was successful
        """
        in_degrees = {k: 0 for k in range(numCourses)}
        edges = {}
        for prereq in prerequisites:
            a, b = prereq
            if a not in edges:
                edges[a] = {}
            edges[a][b] = True
            in_degrees[b] += 1

        queue = deque([k for k, v in in_degrees.items() if v == 0])
        result = []
        while queue:
            current_node = queue.popleft()
            result.append(current_node)
            if neighbor not in edges:
                continue
            for neighbor in edges[current_node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        return len(result) == numCourses
