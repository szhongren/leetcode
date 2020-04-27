"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
"""

import random as rnd

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def make_list(a):
    out = []
    while a > 0:
        digit = a % 10
        a = a // 10
        out.append(ListNode(digit))
    for i in range(len(out) - 1):
        out[i].next = out[i + 1]
    return out[0]

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.len = 0
        curr = self.head
        while curr != None:
            self.len += 1
            curr = curr.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        rnd.seed()
        curr = self.head
        stop = rnd.randrange(self.len)
        while stop != 0:
            stop -= 1
            curr = curr.next
        return curr.val

ans = Solution(make_list(54321))
res = []
for _ in range(10000):
    res.append(ans.getRandom())
for i in range(1, 6):
    print("{}: {}", i, res.count(i))
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()