"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def make_tree(ls):
    """
    :type ls: List[int]
    :rtype: TreeNode
    """
    list_nodes = list(map(lambda x: TreeNode(x) if x != None else None, ls))
    length = len(list_nodes)
    for i in range(length // 2):
        if list_nodes[i] != None:
            if i * 2 + 1 < length:
                list_nodes[i].left = list_nodes[i * 2 + 1]
            if i * 2 + 2 < length:
                list_nodes[i].right = list_nodes[i * 2 + 2]
    return list_nodes[0]

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = [root]

    def hasNext(self):
        """
        :rtype: bool
        """
        return not (len(self.stack) == 1 and self.stack[0] == None)

    def next(self):
        """
        :rtype: int
        """
        none_found = False
        while not none_found:
            curr = self.stack[-1]
            self.stack = self.stack[:-1]
            if curr == None:
                none_found = True
            else:
                self.stack.append(curr.right)
                self.stack.append(curr)
                self.stack.append(curr.left)
        res = self.stack[-1]
        self.stack = self.stack[:-1]
        return res.val

ans = BSTIterator(make_tree([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]))
while ans.hasNext():
    print(ans.next())
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())