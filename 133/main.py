from typing import Optional
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        approach
        do a bfs, to get all the nodes and the edges
        rebuild a new graph
        """
        if node is None:
            return None
        nodes = set()
        edges = set()
        queue = deque()
        queue.append(node)
        while queue:
            current_node = queue.popleft()
            if current_node.val not in nodes:
                nodes.add(current_node.val)
            for neighbor in current_node.neighbors:
                edges.add((current_node.val, neighbor.val))
                if neighbor.val not in nodes:
                    queue.append(neighbor)

        nodes_map = {k: Node(k) for k in nodes}
        for edge in edges:
            a, b = edge
            nodes_map[a].neighbors.append(nodes_map[b])
        return nodes_map[node.val]
