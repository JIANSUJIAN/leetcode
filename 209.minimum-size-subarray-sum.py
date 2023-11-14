#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start

class Solution:
    from sys import maxsize

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Finds the minimal length of a subarray with a sum greater than or equal to the target value.
        
        Args:
        - target: Target sum value.
        - nums: List of integers.
        
        Returns:
        The minimal length of a subarray with a sum greater than or equal to target. If no such subarray exists, returns 0.
        """

        # Initialize the minimal length to a large value, the left pointer, and the running total of the subarray.
        min_length = maxsize
        left_pointer, current_sum = 0, 0

        # Iterate through the nums list.
        for right_pointer in range(len(nums)):
            # Incrementally update the sum as we expand the subarray to the right.
            current_sum += nums[right_pointer]

            # Check if the current subarray's sum meets or exceeds the target.
            while current_sum >= target:
                # Update the minimal length if the current subarray is shorter.
                min_length = min(min_length, right_pointer - left_pointer + 1)

                # Reduce the sum by removing the leftmost element of the subarray.
                current_sum -= nums[left_pointer]

                # Move the left pointer to the right.
                left_pointer += 1

        # If min_length remains unchanged (no subarray found), return 0. Otherwise, return min_length.
        return min_length if min_length != maxsize else 0

        
# @lc code=end

