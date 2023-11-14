#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Initialize a pointer to the start of the list
        pointer = 0 
        
        # Traverse through the list
        for i in range(len(nums)):
            # If the current element is not a zero,
            # move it to the position indicated by the 'pointer'
            # and then move the 'pointer' to the next position.
            if nums[i] != 0:
                nums[pointer] = nums[i]
                pointer += 1

        # After processing all the non-zero elements,
        # fill in the rest of the array with zeros.
        for i in range(pointer, len(nums)):
            nums[i] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pointer = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1

 

# 2. two pointers
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = self.removeElement(nums, 0)

        for i in range(p, len(nums)):
            nums[i] = 0
    
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

        
# @lc code=end

