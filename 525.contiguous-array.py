#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start

# Related to 560 and 325
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Initialize running_sum to index mapping, with -1 for running_sum 0.
        sum_index_map = {0: -1}
        # Initialize variables. max_length stores the result, and running_sum is the running sum.
        max_length = running_sum = 0
        
        for index, num in enumerate(nums):
            # Increment or decrement running_sum based on the value of nums[i]
            running_sum = running_sum + 1 if num else running_sum - 1
            
            # Check if this running_sum has been seen before
            if running_sum in sum_index_map:
                # If so, max_length is the max of its current value and the difference
                # between the current index and the first index this running_sum was seen
                max_length = max(max_length, index - sum_index_map[running_sum])
            else:
                # Otherwise, add this running_sum with its index to the map
                sum_index_map[running_sum] = index
        
        return max_length

        
# @lc code=end

