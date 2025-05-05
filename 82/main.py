from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        approach
        for each new number, look for the next number
        -> store current num
        fast pointer go to next until null or different number
        set current to fast_pointer
        recurse
        """

        def deleteDuplicatesRecur(head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None:
                return head
            curr, fast = head, head
            count = 0
            while fast is not None and fast.val == curr.val:
                fast = fast.next
                count += 1
            curr.next = deleteDuplicatesRecur(fast)
            return curr.next if count > 1 else curr

        return deleteDuplicatesRecur(head)


"""
edge cases
[]
[1]
[1, 1, 1]
[1, 2]
[1, 2, 2, 3]
"""
