"""
Given a linked list, remove the nth node from the end of list and return its head.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        curr = head
        tail = head
        for i in range(n):
            curr = curr.next
        if curr == None:
            return head.next
        while curr.next != None:
            curr = curr.next
            tail = tail.next
        tail.next = tail.next.next
        return head

def makeNumber(a):
    out = []
    while a > 0:
        digit = a % 10
        a = a // 10
        out.append(ListNode(digit))
    for i in range(len(out) - 1):
        out[i].next = out[i + 1]
    return out[0]

ans = Solution()
new = ans.removeNthFromEnd(makeNumber(21), 1)
new2 = ans.removeNthFromEnd(makeNumber(1), 1)
new3 = ans.removeNthFromEnd(None, 0)
new4 = ans.removeNthFromEnd(makeNumber(21), 2)
pass