"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "[" + str(self.val) + "]->" + str(self.next)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_list(ls):
    new = list(map(ListNode, ls))
    for i in range(len(new) - 1):
        new[i].next = new[i+1]
    return new[0]

def del_last(ll):
    if ll == None or ll.next == None:
        return None
    else:
        curr = ListNode(ll.val)
        curr.next = del_last(ll.next)
        return curr

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        else:
            fast = head
            slow = head
            left = ListNode(slow.val)
            copy = left
            while fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
                copy.next = ListNode(slow.val)
                copy = copy.next
            left = del_last(left)
            curr = TreeNode(slow.val)
            curr.left = self.sortedListToBST(left)
            curr.right = self.sortedListToBST(slow.next)
            return curr

ans = Solution()
print(ans.sortedListToBST(make_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])))