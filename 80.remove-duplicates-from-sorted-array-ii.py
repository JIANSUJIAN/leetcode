#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: if nums is empty
        if len(nums) == 0:
            return 0

        # Initialize two pointers, 'slow' to track the position of the last modified value 
        # and 'fast' to scan through the nums list
        slow = 0
        fast = 0

        # 'count' keeps track of the number of occurrences of the current number
        count = 0

        while fast < len(nums):
            # If the current number at the 'fast' pointer is different from 
            # the one at the 'slow' pointer, move the 'slow' pointer ahead 
            # and update the value at the 'slow' pointer
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            
            # If current number is same but has occurred less than 2 times,
            # update the value at the 'slow' pointer and move 'slow' ahead
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]

            # Move the 'fast' pointer ahead
            fast += 1
            
            # Increase the count of occurrences of the current number
            count += 1

            # If a new number is encountered at the 'fast' pointer,
            # reset the 'count' to 0
            if fast < len(nums) and nums[fast] != nums[fast - 1]:
                count = 0

        # Return the length of the modified nums list
        return slow + 1


                

            
            
        
# @lc code=end

