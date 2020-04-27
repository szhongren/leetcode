"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
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

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            left = [root.left]
            right = [root.right]
            none_found = False
            while len(left) == len(right) and len(left) != 0:
                l_curr = left[-1]
                left = left[:-1]
                r_curr = right[-1]
                right = right[:-1]
                if l_curr == None and r_curr == None:
                    none_found = True
                elif l_curr == None:
                    return False
                elif r_curr == None:
                    return False
                elif none_found:
                    print("Comparing {} to {}".format(r_curr.val, l_curr.val))
                    if l_curr.val != r_curr.val:
                        return False
                    none_found = False
                else:
                    right.append(r_curr.right)
                    right.append(r_curr)
                    right.append(r_curr.left)

                    left.append(l_curr.left)
                    left.append(l_curr)
                    left.append(l_curr.right)
            if len(left) != len(right):
                return False
            else:
                return True

def inOrderTraversal(root):
    res = []
    stack = [root]
    none_found = False
    while len(stack) > 0:
        curr = stack[-1]
        stack = stack[:-1]
        if curr == None:
            none_found = True
        elif none_found:
            res.append(curr.val)
            none_found = False
        else:
            stack.append(curr.right)
            stack.append(curr)
            stack.append(curr.left)
    return res

ans = Solution()
print(ans.isSymmetric(make_tree([1,2,2,3,4,4,3])))
print(ans.isSymmetric(make_tree([1,2,3,3,None,2,None])))