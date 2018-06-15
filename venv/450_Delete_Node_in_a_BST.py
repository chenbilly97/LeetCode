# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if (root == None):
            return root
        if (root.val < key):
            root.right = self.deleteNode(root.right, key)
        elif (root.val > key):
            root.left = self.deleteNode(root.left, key)
        else:
            if (root.left == None and root.right == None):
                return None
            elif (root.left == None):
                return root.right
            elif (root.right == None):
                return root.left
            else:
                min = root.right
                while (min.left != None):
                    min = min.left
                root.val = min.val
                root.right = self.deleteNode(root.right, min.val)
        return root
