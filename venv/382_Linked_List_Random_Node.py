# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.h = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        index = 0
        cur = self.h
        val = cur.val
        while (not cur == None):
            if (random.randint(0, index) == index):
                val = cur.val
            cur = cur.next
            index += 1
        return val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()