"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "[" + str(self.val) + "]->" + str(self.next)

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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # trick solution, transform the problem into the find cycle problem by linking the end of 1`lits to its start
        if headA == None or headB == None:
            return None
        ap = headA
        a = []
        while ap != None:
            a.append(ap)
            ap = ap.next
        bp = headB
        b = []
        while bp != None:
            b.append(bp)
            bp = bp.next
        res = None
        for (ai, bi) in zip(range(len(a) - 1, -1, -1), range(len(b) - 1, -1, -1)):
            if a[ai].val == b[bi].val:
                res = a[ai]
            else:
                break
        return res

def make_list(ls):
    new = list(map(ListNode, ls))
    for i in range(len(new) - 1):
        new[i].next = new[i+1]
    return new[0]

ans = Solution()
print(make_list([1, 2, 3, 4, 12, 9, 1283]))
print(ans.getIntersectionNode(makeNumber(12345), makeNumber(67890)))
print(ans.getIntersectionNode(makeNumber(12345), makeNumber(1236789)))