from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        approach
        count in_degree of nodes
        set up base cases, zero in_degrees
        then, for i in range(n):
            result.append(find_parents(i))
        find_parents is memoized, and its ancestors are just the nodes that point to it + the ancestors of the nodes that point to it, recursively
        """

        parents = {node: set() for node in range(n)}
        for source, target in edges:
            parents[target].add(source)

        results = {node: set() for node in range(n) if len(parents[node]) == 0}

        def get_ancestors(node: int):
            if node in results:
                return results[node]
            result = set()
            for source in parents[node]:
                result.add(source)
                result = result.union(get_ancestors(source))
            results[node] = result
            return results[node]

        result = []
        for i in range(n):
            result.append(sorted(list(get_ancestors(i))))
        return result


sol = Solution()
print(
    sol.getAncestors(
        8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
    )
)
