#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers: slow and fast both at the beginning of the array.
        slow, fast = 0, 0
        
        # Iterate through the list with the fast pointer.
        while fast < len(nums):
            # If the current element (nums[fast]) is not the target value (val)...
            if nums[fast] != val:
                # ...copy it to the position of the slow pointer.
                nums[slow] = nums[fast]
                # Increment the slow pointer.
                slow += 1
            
            # Always increment the fast pointer to process the next element.
            fast += 1
        
        # Return the new length of the modified array.
        return slow

        
# @lc code=end

