class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        res = [];
        for i in range(0,length):
            for j in range (i+1,length):
                if nums[i]+nums[j]==target:
                    res.append(i)
                    res.append(j)
        return res
