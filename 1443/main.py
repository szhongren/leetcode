from typing import List, Set, Tuple


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        approach:
        check if subgraph has apple, if yes, add 2 to total for going to and back from subtree, add all across all branches
        """
        edges_map = {}
        for a, b in edges:
            if a not in edges_map:
                edges_map[a] = set()
            edges_map[a].add(b)
            if b not in edges_map:
                edges_map[b] = set()
            edges_map[b].add(a)

        def minTimeRecur(node: int, parent: int):
            if node not in edges_map:
                return 0, hasApple[node]
            total_time_required = 0
            apple_in_subtree = False
            for next_node in edges_map.get(node, set()):
                if next_node == parent:
                    continue
                time_required_for_subtree, subtree_has_apple = minTimeRecur(
                    next_node, node
                )
                if subtree_has_apple:
                    # magic number
                    total_time_required += time_required_for_subtree + 2
                    # need to set it here so that if any subtree has apple the the root should return True
                    apple_in_subtree = subtree_has_apple
            return (total_time_required, hasApple[node] or apple_in_subtree)

        return minTimeRecur(0, -1)[0]
