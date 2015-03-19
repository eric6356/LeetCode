# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
def preListGen(root):
    if root:
        yield [root.val]
        for x in preListGen(root.left):
            yield x
        for x in preListGen(root.right):
            yield x
# @param root, a tree node
# @return a list of integers
def preorderTraversal(root):
    r = list()
    for i in preListGen(root):
        print i
        r += i
    return r

a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(1)
a.left = b
b.right = c

print preorderTraversal(a)