# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        ceng = 0
        qc = [root]
        qn = list()
        while True:
            while qc:
                cur = qc.pop()
                if not cur.left and not cur.right:
                    return ceng
                if cur.left:
                    qn.append(cur.left)
                if cur.right:
                    qn.append(cur.right)
            ceng+=1
            qc = qn
            qn = list()