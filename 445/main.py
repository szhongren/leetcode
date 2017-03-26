"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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

def append(l0, l1):
    """
    appends list to another list
    :type l0: ListNode
    :type l1: ListNode
    :rtype: ListNode
    """
    if l0 == None:
        return l1
    l0.next = append(l0.next, l1)
    return l0

def padZeros(ls, count):
    if count == 0:
        return ls
    curr = ListNode(0)
    curr.next = padZeros(ls, count -1)
    return curr

def getLength(ls, acc=0):
    """
    tail recursive length func
    :type ls: ListNode
    :type acc: int
    :rtype: int
    """
    if ls == None:
        return acc
    return getLength(ls.next, acc + 1)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = getLength(l1)
        len2 = getLength(l2)
        if len1 > len2:
            return self.addTwoNumbers(l2, l1)
        extra_digits = len2 - len1
        l1 = padZeros(l1, extra_digits)
        def addDigitRecur(d0, d1):
            """
            :type d0: ListNode
            :type d1: ListNode
            :rtype: ListNode
            """
            if d0.next == None and d1.next == None:
                return ListNode(d0.val + d1.val)
            next_digit = addDigitRecur(d0.next, d1.next)
            curr = ListNode(d0.val + d1.val + next_digit.val // 10)
            next_digit.val %= 10
            curr.next = next_digit
            return curr
        summed = addDigitRecur(l1, l2)
        carry = summed.val // 10
        summed.val %= 10
        if carry:
            first_digit = ListNode(carry)
            first_digit.next = summed
        else:
            first_digit = summed
        return first_digit

ans = Solution()
print(ans.addTwoNumbers(make_list([7, 2, 4, 3]), make_list([5, 6, 4])))
