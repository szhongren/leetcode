"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        else:
            odd_p = head
            even_p = odd_p.next
            odd_head = odd_p
            even_head = even_p
            curr_is_odd = True
            while odd_p != None and even_p != None:
                if curr_is_odd:
                    odd_p.next = even_p.next
                    odd_p = even_p.next
                else:
                    even_p.next = odd_p.next
                    even_p = odd_p.next
                curr_is_odd = not curr_is_odd
            odd_p = odd_head
            while odd_p.next != None:
                odd_p = odd_p.next
            odd_p.next = even_head
            return odd_head


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
print(ans.oddEvenList(None))
print(ans.oddEvenList(makeNumber(1)))
print(ans.oddEvenList(makeNumber(21)))
print(ans.oddEvenList(makeNumber(321)))
print(ans.oddEvenList(makeNumber(4321)))
print(ans.oddEvenList(makeNumber(54321)))