# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left:
            if root.right.left or root.right.left:
                return False
            return True
        if not root.right:
            if root.left.left or root.left.right:
                return False
            return True
        if root.right.left or root.right.left:
            return self.isBalanced(root.right)
        if root.left.left or root.left.right:
            return self.isBalanced(root.left)
        return True

