# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if (root == None):
            return root
        root1 = TreeNode(root.val)
        root1.right = self.invertTree(root.left)
        root1.left = self.invertTree(root.right)
        return root1
