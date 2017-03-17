# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def make_list_from_num(a):
    out = []
    while a > 0:
        digit = a % 10
        a = a // 10
        out.append(ListNode(digit))
    for i in range(len(out) - 1):
        out[i].next = out[i + 1]
    return out[0]

def make_list(ls):
    if len(ls) == 0:
        return None
    list_nodes = list(map(lambda x: ListNode(x), ls))
    for i, v in enumerate(list_nodes[1:]):
        list_nodes[i].next = v
    return list_nodes[0]

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
