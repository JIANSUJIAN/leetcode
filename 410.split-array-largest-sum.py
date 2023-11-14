#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List

class Solution:
    def num_partitions(self, nums, x) -> int:
        """Calculate the number of partitions needed given a maximum sum limit 'x'."""
        partitions = 0
        i = 0
        while i < len(nums):
            current_sum = 0
            while i < len(nums) and current_sum + nums[i] <= x:
                current_sum += nums[i]
                i += 1
            partitions += 1
        return partitions

    def splitArray(self, nums: List[int], k: int) -> int:
        """Determine the maximum sum of a subarray when the array 'nums' is split into 'k' subarrays."""
        
        # Initialize the left boundary with the maximum number in 'nums'. 
        # This is because any partition should at least be able to hold the largest element.
        left = max(nums)  
        
        # Initialize the right boundary with the total sum of 'nums'.
        # This represents the sum if all numbers were in a single partition.
        right = sum(nums) + 1

        # Binary search to find the smallest maximum subarray sum.
        while left < right:
            mid = left + (right - left) // 2
            partitions_needed = self.num_partitions(nums, mid)
            
            # Adjust the search space based on the number of partitions needed with the current 'mid' value.
            if partitions_needed > k:
                left = mid + 1
            else:
                right = mid
                
        return left

# @lc code=end

