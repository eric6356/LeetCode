# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, node):
        if not node:
            return 0
        ldepth = self.depth(node.left)
        rdepth = self.depth(node.right)
        return max(ldepth, rdepth) + 1
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return self.depth(root)
