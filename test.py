class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def proc(node, stk, res):
    stk.append(node.val)
    tmp = 0
    if node.left:
        proc(node.left, stk, res)
    if node.right:
        proc(node.right, stk, res)
    if not node.left and not node.right:
        for i in stk:
            tmp *= 10
            tmp += i
        # print stk, node.val, res, tmp
        stk.pop()
        res[0] += tmp
        return res[0]
    stk.pop()
    return res[0]
# @param root, a tree node
# @return an integer
def sumNumbers(root):
    if not root:
        return 0
    stk = list()
    res = [0]
    return proc(root, stk, res)


root = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)

root.left = l2
root.right = l3
l2.right = l4

r = TreeNode(0)
print sumNumbers(r)