class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def proc(node, stk, res):
    if node.left:
        stk.append(node.left.val)
        res += proc(node.left, stk, res)
        stk.pop()
    elif node.right:
        stk.append(node.right.val)
        res += proc(node.right, stk, res)
        stk.pop()
    # if not node.left and not node.right:
    else:
        tmp = 0
        print stk, node.val, res
        for i in stk:
            tmp *= 10
            tmp += i
        return tmp
    return res
# @param root, a tree node
# @return an integer
def sumNumbers(root):
    if not root:
        return 0
    stk = [root.val]
    res = 0
    return proc(root, stk, res)


root = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)

root.left = l2
root.right = l3
l3.right = l4
print sumNumbers(root)