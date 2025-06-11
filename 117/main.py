from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        """
        approach
        bfs
        each level, set the next pointers
        return root
        """
        if root is None:
            return None
        queue = deque([root])
        while queue:
            new_queue = deque()
            next_node = None
            for i in range(len(queue) - 1, -1, -1):
                node = queue[i]
                node.next = next_node
                next_node = node
                if node.right:
                    new_queue.appendleft(node.right)
                if node.left:
                    new_queue.appendleft(node.left)
            queue = new_queue
        return root
