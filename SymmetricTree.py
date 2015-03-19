# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hper(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and not t2 or t2 and not t1:
            return False
        if t1.val != t2.val:
            return False
        if (t1.left and not t2.right) or (t1.right and not t2.left):
            return False
        return self.hper(t1.left, t2.right) and self.hper(t1.right, t2.left)
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return None
        return self.hper(root.left, root.right)
