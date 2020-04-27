"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""

# use 4 pointers, curr_p, prev_p, curr_head, prev_head
# since we assume perfect binary tree, makes things a lot easier, but if it was not perfert, we'd just have to go through the previous level to find the next node anyway'

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.val) + "\n " + str(self.left) + ' ' + str(self.right)

def make_tree(ls):
    """
    :type ls: List[int]
    :rtype: TreeNode
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

"""
    TreeLinkNode lastHead = root;//prevous level's head
    TreeLinkNode lastCurrent = null;//previous level's pointer
    TreeLinkNode currentHead = null;//currnet level's head
    TreeLinkNode current = null;//current level's pointer

    while(lastHead!=null){
        lastCurrent = lastHead;

        while(lastCurrent!=null){
            if(currentHead == null){
                currentHead = lastCurrent.left;
                current = lastCurrent.left;
            }else{
                current.next = lastCurrent.left;
                current = current.next;
            }

            if(currentHead != null){
                current.next = lastCurrent.right;
                current = current.next;
            }

            lastCurrent = lastCurrent.next;
        }

        //update last head
        lastHead = currentHead;
        currentHead = null;
    }
"""
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return None

        else:
            prev_head = root
            prev_p = None
            curr_head = None
            curr_p = None
            # when prev_head == None, we are one level below the end of the tree
            while prev_head != None:
                # init prev_p
                prev_p = prev_head
                # while it has not reached the end of the level
                while prev_p != None:
                    # if curr_head == None, we init it and curr_p
                    if curr_head == None:
                        curr_head = prev_p.left
                        curr_p = prev_p.left
                    # if its not None, we are at the right subchild of prev_p
                    else:
                        curr_p.next = prev_p.left
                        curr_p = curr_p.next
                    # if curr_head is not None, we are at the left subchild of prev_p
                    if curr_head != None:
                        curr_p.next = prev_p.right
                        curr_p = curr_p.next
                    # move right
                    prev_p = prev_p.next
                # move down
                prev_head = curr_head
                curr_head = None
        return root

ans = Solution()
print(ans.connect(make_tree([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])))