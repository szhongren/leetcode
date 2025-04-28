from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        approach
        rebuild as graph
        bfs
        """
        nodes = set()
        edges = {}

        def build_graph(root: TreeNode, parent: int):
            if root is None:
                return
            nodes.add(root.val)
            if parent is not None:
                if root.val not in edges:
                    edges[root.val] = {}
                edges[root.val][parent] = True
                if parent not in edges:
                    edges[parent] = {}
                edges[parent][root.val] = True
            build_graph(root.left, root.val)
            build_graph(root.right, root.val)

        build_graph(root, None)

        queue = []
        queue.append(target.val)
        seen = set()
        while queue:
            if k == 0:
                return queue
            new_queue = []
            for node in queue:
                seen.add(node)
                if node not in edges:
                    continue
                for next_node in edges[node].keys():
                    if next_node in seen:
                        continue
                    new_queue.append(next_node)
            queue = new_queue
            k -= 1
        return []
