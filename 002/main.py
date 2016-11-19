"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return add_carry(l1, l2, 0)

def add_carry(l1, l2, c):
    if l1 == None and l2 == None:
        if c == 0:
            return None
        else:
            return ListNode(c)
    elif l1 == None:
        digit = l2.val + c
        ans = ListNode(digit % 10)
        ans.next = add_carry(None, l2.next, digit // 10)
        return ans
    elif l2 == None:
        digit = l1.val + c
        ans = ListNode(digit % 10)
        ans.next = add_carry(l1.next, None, digit // 10)
        return ans
    else:
        digit = l1.val + l2.val + c
        ans = ListNode(digit % 10)
        ans.next = add_carry(l1.next, l2.next, digit // 10)
        return ans


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
print(ans.addTwoNumbers(makeNumber(342), makeNumber(465)))
