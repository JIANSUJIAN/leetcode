#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Get the length of the input list
        n = len(nums)
        
        # Initialize the duplicate variable
        dup = -1
        
        # Identify the duplicate number:
        # By traversing the list and marking visited numbers as negative,
        # we can find the duplicate number when encountering a negative value.
        for i in range(n):
            # Derive an index from the current number's absolute value
            index = abs(nums[i]) - 1
            
            # If the number at the derived index is negative, 
            # then the current number is a duplicate.
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                # Otherwise, negate the number at the derived index to mark it as visited.
                nums[index] *= -1
        
        # Initialize the missing number variable
        missing = -1
        
        # Identify the missing number:
        # After the above loop, the only positive number indicates
        # the position (or index + 1) of the missing number.
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        
        # Return the identified duplicate and missing numbers
        return [dup, missing]




        
# @lc code=end

