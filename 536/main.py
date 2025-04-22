from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def split_into_subtree_strs(s: str) -> Tuple[str, str]:
            count = 0
            for i in range(len(s)):
                if s[i] == "(":
                    count += 1
                elif s[i] == ")":
                    count -= 1
                if count == 0:
                    return s[1:i], s[i + 2 : -1]

        if s == "":
            return None
        index = s.find("(")
        if index == -1:
            return TreeNode(int(s))
        subtree_a, subtree_b = split_into_subtree_strs(s[index:])
        return TreeNode(
            int(s[:index]), self.str2tree(subtree_a), self.str2tree(subtree_b)
        )
