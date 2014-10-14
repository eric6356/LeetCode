class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def compare(p, q):
    if p and q and p.val != q.val:
        return False
    elif (p and not q) or (q and not p):
        return False
    elif not p and not q:
        return None
    if compare(p.left, q.left) is False:
        return False
    if compare(p.right, q.right) is False:
        return False
    return True
# @param p, a tree node
# @param q, a tree node
# @return a boolean
def isSameTree(p, q):
    if compare(p, q) is False:
        return False
    return True

qt = TreeNode(0)
pt = None
print qt and not pt
print isSameTree(pt, qt)