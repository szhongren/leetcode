"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # tree = preorder.split(',')
        # while len(tree) > 2:
        #     pos = len(tree) - 3
        #     while pos > -1:
        #         root = tree[pos]
        #         left = tree[pos + 1]
        #         right = tree[pos + 2]
        #         if root != '#' and left == '#' and right == '#':
        #             tree = tree[:pos] + ['#'] + tree[pos + 3:]
        #             break
        #         pos -= 1
        #     # do things
        #     if pos == -1:
        #         return False

        # if len(tree) == 2:
        #     return False
        # return tree[0] == '#'
        stack0 = preorder.split(',')
        stack1 = []
        while len(stack0) > 2:
            for _ in range(len(stack0)):
                stack1.append(stack0.pop())
                if len(stack1) < 3:
                    continue
                root = stack1[-1]
                left = stack1[-2]
                right = stack1[-3]
                if root != '#' and left == '#' and right == '#':
                    stack0.append('#')
                    for _ in range(3):
                        stack1.pop()
                    while len(stack1) > 0:
                        stack0.append(stack1.pop())
                    break
            if len(stack0) == 0:
                return False

        if len(stack0) == 2:
            return False
        return stack0[0] == '#'



ans = Solution()
print(ans.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

print(ans.isValidSerialization("1,#"))

print(ans.isValidSerialization("9,#,#,1"))

