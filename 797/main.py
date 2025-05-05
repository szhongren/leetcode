from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        approach
        bfs recur
        if target:
            return [[3]]
        else:
            if recursive returns not empty list, for every item in return, add current to left
        """

        n = len(graph)
        paths = {}
        for i, edges in enumerate(graph):
            paths[i] = set(edges)

        def allPathsSourceTarget(current: int):
            if current == n - 1:
                return [[n - 1]]

            result = []
            for to in paths[current]:
                recur = allPathsSourceTarget(to)
                result += [[current] + res for res in recur]
            return result

        return allPathsSourceTarget(0)


sol = Solution()
print(sol.allPathsSourceTarget([[1, 2], [3], [3], []]))
