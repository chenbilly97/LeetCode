class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        res[0] = 1
        lenN = len(nums)
        for i in range(1, lenN):
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in reversed(range(0, lenN)):
            res[i] = res[i] * right
            right = right * nums[i]

        return res
