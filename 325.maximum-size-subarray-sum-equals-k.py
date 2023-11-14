#
# @lc app=leetcode id=325 lang=python3
#
# [325] Maximum Size Subarray Sum Equals k
#

# @lc code=start

# Combination of [560] and [525]
class Solution:
    def findMaxLength(self, nums: List[int], k: int) -> int:
        # Initialize running_sum to index mapping with 0: -1.
        sum_index_map = {0: -1}
        max_length = running_sum = 0
        
        for index, num in enumerate(nums):
            # Increment running_sum based on the value of nums[i]
            running_sum += num
            
            # The sum we need to find in sum_index_map to ensure there exists a subarray
            # nums[i:j] such that its sum is k, where i is a stored index and j is the current index.
            sum_to_find = running_sum - k
            
            # If sum_to_find exists in the map, calculate and update max_length.
            if sum_to_find in sum_index_map:
                max_length = max(max_length, index - sum_index_map[sum_to_find])
            
            # If running_sum not in map, add it.
            if running_sum not in sum_index_map:
                sum_index_map[running_sum] = index
        
        return max_length


            
        
# @lc code=end

