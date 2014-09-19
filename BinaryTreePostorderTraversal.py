class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        r = list()
        if root:
            if root.left:
                r += self.postorderTraversal(root.left)
            if root.right:
                r += self.postorderTraversal(root.right)
            r.append(root.val)
        return r