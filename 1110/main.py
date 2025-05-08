from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        """
        approach
        recursive
        at each node
        if none:
            return None
        for left, right
            if child is None:
                pass
            if child to delete:
                child = None
                return [recur(child.left), recur(child.right)]
            else:
                recur(child)
        """
        to_delete = set(to_delete)

        results = []

        def delNodes(root: Optional[TreeNode], parent_deleted: bool):
            if root is None:
                return
            if parent_deleted:
                if root.val not in to_delete:
                    results.append(root)
            delNodes(root.left, root.val in to_delete)
            if root.left and root.left.val in to_delete:
                root.left = None
            delNodes(root.right, root.val in to_delete)
            if root.right and root.right.val in to_delete:
                root.right = None

        delNodes(root, True)
        return results
