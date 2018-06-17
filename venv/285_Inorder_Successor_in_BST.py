# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        queue = []
        self.dfs(root, p, queue)
        if (len(queue) >= 2 and queue[-2] == p):
            return queue[-1]
        else:
            return None

    def dfs(self, root, p, queue):
        if (root == None):
            return
        self.dfs(root.left, p, queue)
        if (len(queue) >= 2 and queue[-2] == p):
            return
        queue.append(root)
        self.dfs(root.right, p, queue)

