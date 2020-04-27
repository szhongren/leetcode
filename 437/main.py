"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
    def pathSum(self, root, k):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        sum_root = self.sumFromRoot(root, 0)
        self.count = 0
        self.countSums(sum_root, [0], k) # small thing  to remember, edge case where the entire path to leaf sums to k
        return self.count

    def sumFromRoot(self, root, acc):
        if root == None:
            return None
        new_root = TreeNode(acc + root.val)
        new_root.left = self.sumFromRoot(root.left, acc + root.val)
        new_root.right = self.sumFromRoot(root.right, acc + root.val)
        return new_root

    def countSums(self, root, prev, k):
        if root == None:
            return
        curr_val = root.val
        for v in prev:
            if curr_val - v == k:
                self.count += 1
        self.countSums(root.left, prev + [curr_val], k)
        self.countSums(root.right, prev + [curr_val], k)

ans = Solution()
print(ans.pathSum(make_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8))
