class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1
        while (left + 1 < right):
            mid = left + (int)((right - left) / 2)
            if (nums[mid] == target):
                return True
            if (nums[left] < nums[mid]):
                if (nums[left] <= target and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
            elif (nums[left] > nums[mid]):
                if (nums[mid] < target and target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        if nums[left] == target or nums[right] == target:
            return True
        else:
            return False
