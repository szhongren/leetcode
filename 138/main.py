from typing import Optional


class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        approach
        * dfs or bfs, dfs for recursive call
        * go and instantiate all the next nodes first, then on the way back up we'll have a node map, we can then set the random pointers
        """

        node_map = {}

        def copyRandomListRecur(head: Optional[Node]) -> Optional[Node]:
            if head is None:
                return head
            new_node = Node(head.val, None, None)
            node_map[head] = new_node
            new_node.next = copyRandomListRecur(new_node.next)
            new_node.random = node_map[head.random]
            return new_node

        return copyRandomListRecur(head)
