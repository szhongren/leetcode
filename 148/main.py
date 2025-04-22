from typing import List, Optional, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        approach
        mergesort
        split into halves, sort those, then merge back together
        """

        def split_list(head: Optional[ListNode]) -> Optional[ListNode]:
            """
            Returns the middle node of the list
            We need a prev pointer to break the list into two parts
            """
            if head is None or head.next is None:
                return None

            # Use prev to track node before slow
            prev = None
            slow = fast = head

            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            # Break the list into two parts
            if prev:
                prev.next = None

            return slow

        def merge_list_recur(
            front: Optional[ListNode], back: Optional[ListNode]
        ) -> Optional[ListNode]:
            if front is None and back is None:
                return None
            if front is None:
                return back
            if back is None:
                return front
            if front.val < back.val:
                front.next = merge_list_recur(front.next, back)
                return front
            else:
                back.next = merge_list_recur(front, back.next)
                return back

        def sort_list_recur(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return None
            if head.next is None:
                return head
            mid = split_list(head)
            sorted_front, sorted_back = sort_list_recur(head), sort_list_recur(mid)
            return merge_list_recur(sorted_front, sorted_back)

        if head is None:
            return head
        return sort_list_recur(head)
