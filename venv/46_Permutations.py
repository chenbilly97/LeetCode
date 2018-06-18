class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if (nums == None or len(nums) == 0):
            return []
        self.helper(nums, 0, [], res, [])
        return res

    def helper(self, nums, index, used, res, list):
        length = len(nums)
        if (index == length):
            res.append(list[:])

        for i in range(length):
            if (not nums[i] in used):
                used.append(nums[i])
                list.append(nums[i])
                self.helper(nums, index + 1, used, res, list)
                list.remove(nums[i])
                used.remove(nums[i])
        return res
