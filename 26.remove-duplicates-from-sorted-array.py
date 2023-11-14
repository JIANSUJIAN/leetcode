#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: if the list is empty, return 0.
        if len(nums) == 0:
            return 0

        # The 'slow' pointer indicates the position of the last unique element.
        slow = 0
        # The 'fast' pointer is used to scan through the list.
        fast = 0

        # Continue until the 'fast' pointer has scanned all elements.
        while fast < len(nums):
            # If the current element (pointed by 'fast') is different from the last unique element (pointed by 'slow')...
            if nums[slow] != nums[fast]:
                # Move 'slow' one step forward.
                slow += 1
                # Copy the unique element from 'fast' position to 'slow' position.
                nums[slow] = nums[fast]
            # Move 'fast' one step forward to continue scanning.
            fast += 1

        # Return the length of the unique elements. As lists are 0-indexed, we add 1 to 'slow'.
        return slow + 1

        
# @lc code=end

