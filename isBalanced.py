class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isb(self, node, res):
    if not node:
        return 0
    lh = self.isb(node.left, res)
    rh = self.isb(node.right, res)
    if abs(lh-rh) > 1:
        res[0] = False
    return max(lh, rh) +1

def isBalanced(self, root):
    res = [True]
    self.isb(root, res)
    return res[0]


r = TreeNode(1)
a = TreeNode(2)
b = TreeNode(3)
r.left = a
a.left = b
print isBalanced(r)