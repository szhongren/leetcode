"""
Sort a linked list using insertion sort.
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
    for i, v in enumerate(list_nodes):
        if i == 0:
            continue
        list_nodes[i - 1].next = v
    return list_nodes[0]

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        last_unsorted = head
        while last_unsorted.next != None:
            last_unsorted = last_unsorted.next
        while head != last_unsorted:
            first = head
            head = head.next
            last_unsorted.next = self.insertIntoSorted(last_unsorted.next, first)
        return self.insertIntoSorted(head.next, head)

    def insertIntoSorted(self, head, node):
        if head == None or head.val >= node.val:
            node.next = head
            return node
        ptr = head
        while ptr.next and ptr.next.val < node.val:
            ptr = ptr.next
        node.next = ptr.next
        ptr.next = node
        return head

ans = Solution()
for i in range(15):
    print(ans.insertIntoSorted(make_list([2, 3, 4, 4, 7, 8, 10, 11]), ListNode(i)))
print(ans.insertionSortList(make_list([2, 7, 64, 3, 0, 46, 15, 1, 2])))
