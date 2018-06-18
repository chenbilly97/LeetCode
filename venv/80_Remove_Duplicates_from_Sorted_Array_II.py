class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) <= 2):
            return len(nums)
        pre = nums[0]
        count = 1
        index = 1
        while index < len(nums):
            if (nums[index] == pre):
                if (count < 2):
                    count += 1
                else:
                    del nums[index]
                    index -= 1
            else:
                pre = nums[index]
                count = 1
            index += 1


