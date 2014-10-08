# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def proc(self, node, stk, res):
        if node.left:
            stk.append(node.left.val)
            res += self.proc(node.left, stk, res)
            stk.pop()
        elif node.right:
            stk.append(node.right.val)
            res += self.proc(node.left, stk, res)
            stk.pop()
        else:
            tmp = 0
            stk.append(node.val)
            for i in stk:
                tmp *= 10
                tmp += i
            res += tmp
            stk.pop()
        return res
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        stk = list()
        res = 0
        return self.proc(root, stk, res)
