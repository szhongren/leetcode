from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_left(root)

    def push_left(self, root: Optional[TreeNode]):
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        next_node = self.stack.pop()
        if next_node.right is not None:
            self.push_left(next_node.right)
        return next_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
