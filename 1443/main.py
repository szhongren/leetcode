from typing import List, Set, Tuple


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        approach:
        check if subgraph has apple, if yes, add 1 to total, add all across all branches
        """
        edges_map = {}
        for a, b in edges:
            if a not in edges_map:
                edges_map[a] = set()
            edges_map[a].add(b)
            if b not in edges_map:
                edges_map[b] = set()
            edges_map[b].add(a)

        def minTimeRecur(node: int, parent: int) -> Tuple[int, bool]:
            total_time_required = 0
            apple_in_subtree = False
            for next_node in edges_map.get(node, set()):
                if next_node == parent:
                    continue
                time_required, has_apple = minTimeRecur(next_node, node)
                if has_apple:
                    total_time_required += time_required + 2
                    apple_in_subtree = True
            return (total_time_required, hasApple[node] or apple_in_subtree)

        result = minTimeRecur(0, -1)
        return result[0]
