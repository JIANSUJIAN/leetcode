#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize the count of subarrays with sum = k to 0
        # Initialize the cumulative sum of elements processed so far to 0
        count, current_sum = 0, 0
        
        # Dictionary to store the frequency of each prefix sum.
        # Initialized with {0: 1} because we have a prefix sum of 0 by default 
        # (before processing any elements).
        preSum = {0: 1}

        # Iterate through each number in the list.
        for num in nums:
            # Update the cumulative sum
            current_sum += num
            
            # Increase count by the number of subarrays ending at the current number 
            # that have a sum of k. If (current_sum - k) exists in preSum, it means 
            # we've seen some prefix of the array with sum (current_sum - k). So, 
            # the numbers between that prefix and the current index form a subarray 
            # with sum = k.
            count += preSum.get(current_sum - k, 0)
            
            # Update the frequency of the current cumulative sum in preSum. 
            # If it doesn't exist, get() will return 0.
            preSum[current_sum] = preSum.get(current_sum, 0) + 1
        
        # Return the total count of subarrays with sum = k.
        return count 

        
# @lc code=end

