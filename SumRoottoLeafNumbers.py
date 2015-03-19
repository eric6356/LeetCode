# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def proc(self, node, stk, res):
        stk.append(node.val)
        tmp = 0
        if node.left:
            self.proc(node.left, stk, res)
        if node.right:
            self.proc(node.right, stk, res)
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
    def sumNumbers(self, root):
        if not root:
            return 0
        stk = list()
        res = [0]
        return self.proc(root, stk, res)