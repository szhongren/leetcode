"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + " => " + str(self.next)

def make_list(ls):
    if len(ls) == 0:
        return None
    list_nodes = list(map(lambda x: ListNode(x), ls))
    for i, v in enumerate(list_nodes[1:]):
        list_nodes[i].next = v
    return list_nodes[0]

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        front_head = ListNode(-1)
        front_iter = front_head
        back_head = ListNode(-1)
        back_iter = back_head
        while head != None:
            if head.val < x:
                front_iter.next = head
                front_iter = front_iter.next
            else:
                back_iter.next = head
                back_iter = back_iter.next
            head = head.next
        back_iter.next = None
        front_iter.next = back_head.next
        return front_head.next

ans = Solution()
print(ans.partition(make_list([1, 4, 3, 2, 5, 2]), 3))

