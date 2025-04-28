from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        approach
        fast slow pointer
        1 2 3 4 5, 2
        remove 4
        1, 1
        1, 2
        1, 3
        1, 4
        move fast > n + 1 times, so that slow points to node right before node to remove
        """
        if head is None:
            return None
        slow, fast = head, head
        while fast != None and n > 0:
            fast = fast.next
            n -= 1
        prev = None
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
        if slow == head:
            return head.next
        prev.next = slow.next
        return head
