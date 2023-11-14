#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers to the start and end of the array
        low, high = 0, len(nums) - 1

        # Continue the search while the low pointer is less than or equal to the high pointer.
        while low <= high:
            # Calculate the mid-point of the current search range.
            mid = (low + high) // 2

            # If the mid-point elelment matches the target, return its index.
            if nums[mid] == target:
                return mid
            
            # Determine if the left portion is sorted.
            if nums[low] <= nums[mid]:
                # Check if target lies within the sorted left portion.
                if nums[low] <= target <= nums[mid]:
                    # Adjust search range to left portion.
                    high = mid - 1
                else:
                    # Adjust search range to the right portion.
                    low = mid + 1
            else: # This means the right portion is sorted.
                # Check if target lies within the right portion.
                if nums[mid] <= target <= nums[high]:
                    # Adjust search range to right portion
                    low = mid + 1
                else:
                    # Adjust search range to left portin.
                    high = mid - 1
        
        # If the loop completes, the target is not present in the array.
        return -1
        
# @lc code=end

