"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # len = 0
        # p = head
        # while p != None:
        #     p = p.next
        #     len += 1
        # for i in range(len // 2):
        #     first = head
        #     last_a = head
        #     last_b = head
        #     for _ in range(i):
        #         first = first.next
        #     for _ in range(i + 1):
        #         last_b = last_b.next
        #     while last_b != None:
        #         last_a = last_a.next
        #         last_b = last_b.next
        #     if first.val != last_a.val:
        #         return False
        # return True
        if head == None or head.next == None:
            return True

        fast = head
        slow = head

        # find midpoint
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        head_b = slow.next
        slow.next = None

        p1 = head_b
        p2 = p1.next

        while p1 != None and p2 != None:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        head_b.next = None

        p = p2
        if p2 == None:
            p = p1
        q = head

        while p != None:
            if p.val != q.val:
                return False

            p = p.next
            q = q.next

        return True



ans = Solution()
print(ans.isPalindrome(makeNumber(123456)))
print(ans.isPalindrome(makeNumber(1234321)))