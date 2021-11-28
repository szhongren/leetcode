# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"<{self.val}: {[neighbor.val for neighbor in self.neighbors]}>"


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        return NodeCloner().clone_node(node)


class NodeCloner:
    def __init__(self):
        self.visited = {}

    def clone_node(self, node: Node) -> Node:
        self.visited[node.val] = Node(node.val)
        self.visited[node.val].neighbors = [
            self.clone_node(neighbor)
            if neighbor.val not in self.visited
            else self.visited[neighbor.val]
            for neighbor in node.neighbors
        ]
        return self.visited[node.val]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
