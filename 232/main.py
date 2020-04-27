"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.on_stack1 = True

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.on_stack1:
            while len(self.stack2) != 0:
                self.stack1.append(self.stack2[-1])
                self.stack2 = self.stack2[:-1]
            self.on_stack1 = True
        self.stack1.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.on_stack1:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1[-1])
                self.stack1 = self.stack1[:-1]
            self.on_stack1 = False
        self.stack2 = self.stack2[:-1]

    def peek(self):
        """
        :rtype: int
        """
        if self.on_stack1:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1[-1])
                self.stack1 = self.stack1[:-1]
            self.on_stack1 = False
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0