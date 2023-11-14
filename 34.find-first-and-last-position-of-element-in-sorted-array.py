#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    
    def left_bound(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        return left
    
    def right_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        return right - 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.left_bound(nums, target)
        right = self.right_bound(nums, target)
        
        if left <= right and left < len(nums) and nums[left] == target:
            return [left, right]

        return [-1, -1]

        
# @lc code=end

