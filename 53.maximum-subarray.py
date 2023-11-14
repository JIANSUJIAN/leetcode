#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Base condition: If the list is empty, return 0
        if not nums:
            return 0

        # Initialize max_current and max_global to the first element of the array
        max_global = max_current = nums[0]

        # Iterate through the list staring from the second element
        for i in range(1, len(nums)):
            # Update max_current for the current position
            max_current = max(nums[i], max_current + nums[i])
            # Whether to start a new subarray with the current element as its only member (if nums[i] is larger), or
            # Whether to extend the previous subarray to include the current element (if max_current + nums[i] is larger).

            # Update max_global if needed
            max_global = max(max_global, max_current)
        
        return max_global


        
# @lc code=end

