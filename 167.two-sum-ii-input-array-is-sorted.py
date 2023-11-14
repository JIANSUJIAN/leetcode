#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers: left at the start and right at the end of the list
        left, right = 0, len(numbers) - 1

        # Continue while the left pointer is to the left of the right pointer
        while left < right:
            # Calculate the sum of the elements pointed to by left and right pointers
            sum = numbers[left] + numbers[right]
            
            # If the sum equals the target, we've found our two numbers
            if sum == target:
                # Return the indices. Note that the question wants 1-based indices, 
                # so we add 1 to each index before returning.
                return [left + 1, right + 1]
            # If the sum is less than the target, move the left pointer to the right 
            # to get a larger sum (since the list is sorted in ascending order)
            elif sum < target:
                left += 1
            # If the sum is greater than the target, move the right pointer to the left
            # to get a smaller sum
            else:
                right -= 1
        
        # If we exit the loop without finding two numbers that add up to the target,
        # return [-1, -1] as an indication that no solution exists.
        return [-1, -1]



        
# @lc code=end

