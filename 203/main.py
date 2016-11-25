"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def makeNumber(a):
    out = []
    while a > 0:
        digit = a % 10
        a = a // 10
        out.append(ListNode(digit))
    for i in range(len(out) - 1):
        out[i].next = out[i + 1]
    return out[0]

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if head == None:
        #     return None
        # elif head.val == val:
        #     return self.removeElements(head.next, val)
        # else:
        #     head.next = self.removeElements(head.next, val)
        #     return head
        helper = ListNode(0)
        helper.next = head
        p = helper

        while p.next != None:
            if p.next.val == val:
                next = p.next
                p.next = next.next
            else:
                p = p.next
        return helper.next


ans = Solution()
print(ans.removeElements(makeNumber(54321), 1))
print(ans.removeElements(makeNumber(11), 1))