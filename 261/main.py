from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        approach
        first, build adjacency tree
        start from any node, do a dfs
        if I ever encounter another node that I've seen before and is not the node I just came from, return False
        """
        adjacency = {i: set() for i in range(n)}
        for a, b in edges:
            adjacency[a].add(b)
            adjacency[b].add(a)

        self.seen = set()
        self.is_tree = True

        def dfs(node: int, prev: int):
            if node in self.seen:
                self.is_tree = False
                return
            self.seen.add(node)
            for next_node in adjacency[node]:
                if next_node == prev:
                    continue
                dfs(next_node, node)

        dfs(0, None)

        return len(self.seen) == n and self.is_tree
