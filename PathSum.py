# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == sum:
                return True
            return False
        if root.left and root.left:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        if root.left:
            return self.hasPathSum(root.left, sum - root.val)
        if root.right:
            return self.hasPathSum(root.right, sum - root.val)