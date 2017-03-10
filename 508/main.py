"""
 Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
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
    if len(ls) == 0:
        return None
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
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.sum_counts = {}
        self.max = 0
        self.findFrequentTreeSumRecur(root)
        return list(set([k for k in self.sum_counts if self.sum_counts[k] == self.max]))

    def findFrequentTreeSumRecur(self, root):
        if root == None:
            return 0
        else:
            sum_here = root.val + self.findFrequentTreeSumRecur(root.left) + self.findFrequentTreeSumRecur(root.right)
            if sum_here in self.sum_counts:
                self.sum_counts[sum_here] += 1
            else:
                self.sum_counts[sum_here] = 1
            self.max = max(self.max, self.sum_counts[sum_here])
            return sum_here


ans = Solution()
print(ans.findFrequentTreeSum(make_tree([5, 2, -3])))

