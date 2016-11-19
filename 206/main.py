"""
Reverse a singly linked list.

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return reverseListHelper(head, None)

def reverseListHelper(first, rest):
    if first == None:
        return rest
    else:
        new_first = first.next
        first.next = rest
        return reverseListHelper(new_first, first)