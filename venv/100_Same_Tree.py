class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q == None):
            return True
        return self.traverseTree(p, q)

    def traverseTree(self, p, q):
        if (p == None and q == None):
            return True
        if (p == None or q == None):
            return False
        if (p.val != q.val):
            return False
        res = True
        res = self.traverseTree(p.left, q.left)
        res = res and self.traverseTree(p.right, q.right)
        return res