"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
class TreeNode:
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

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        self.getPaths(root, "")
        return self.res

    def getPaths(self, root, path):
        """
        :type root: TreeNode
        :rtype: None
        """
        if root == None:
            return
        if path == "":
            path = path + str(root.val)
        else:
            path = path + "->" + str(root.val)

        if root.left == None and root.right == None:
            self.res.append(path)
        else:
            self.getPaths(root.left, path)
            self.getPaths(root.right, path)

ans = Solution()
print(ans.binaryTreePaths(make_tree([1, 2, 3, None, 5])))