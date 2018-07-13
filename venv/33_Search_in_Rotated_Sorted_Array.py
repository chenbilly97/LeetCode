class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        i = 0
        j = len(nums) - 1
        while i + 1 < j:
            m = i + (int)((j - i) / 2)
            if nums[m] == target:
                return m
            else:
                if (nums[i] < nums[m]):
                    if nums[i] <= target and target <= nums[m]:
                        j = m - 1
                    else:
                        i = m + 1
                elif nums[m] < nums[j]:
                    if nums[m + 1] <= target and target <= nums[j]:
                        i = m + 1
                    else:
                        j = m - 1

        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        return -1
