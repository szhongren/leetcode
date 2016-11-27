"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def make_tree(ls):
    """
    :type ls: List[int]
    :rtype: TreeLinkNode
    """
    list_nodes = list(map(lambda x: TreeLinkNode(x) if x != None else None, ls))
    length = len(list_nodes)
    for i in range(length // 2):
        if list_nodes[i] != None:
            if i * 2 + 1 < length:
                list_nodes[i].left = list_nodes[i * 2 + 1]
            if i * 2 + 2 < length:
                list_nodes[i].right = list_nodes[i * 2 + 2]
    return list_nodes[0]

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        return self.levelOrderRecur([root])
        # there is a better way by using 4 ptrs, lastHead, currHead, lastCurr, curr
        # uses O(1) space

    def levelOrderRecur(self, queue):
        queue = list(filter(lambda x: x != None, queue))
        for i in range(len(queue) - 1):
            queue[i].next = queue[i + 1]
        new_queue = []
        while len(queue) != 0:
            curr = queue[0]
            queue = queue[1:]
            print(curr.val)
            new_queue.append(curr.left)
            new_queue.append(curr.right)
        if len(new_queue) != 0:
            self.levelOrderRecur(new_queue)




ans = Solution()
print(ans.connect(make_tree([1, 2, 3, 4, 5, None, 7])))