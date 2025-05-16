from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        """
        approach
        edge case:
        empty list, return item with itself as next
        slow = head, fast = head.next
        advance until slow <= val and fast >= val
        edge case: back of list
        or if slow <= val and fast < val
        add the node
        new_next = slow.next
        slow.next = new node(val)
        slow.next.next = new_next
        return head
        edge case: front of list
        """
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        slow, fast = head, head.next
        if slow == fast:
            head.next = Node(insertVal)
            head.next.next = head
            return head
        while True:
            if slow.val <= insertVal and fast.val >= insertVal:
                break
            if slow.val > fast.val and insertVal <= fast.val:
                break
            if slow.val > fast.val and insertVal >= slow.val:
                break
            slow, fast = slow.next, fast.next
            if head == slow:
                break
        next_next = slow.next
        slow.next = Node(insertVal)
        slow.next.next = next_next
        return head
