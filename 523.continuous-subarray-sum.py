#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Initialize a hashmap to store (prefix sum modulo k, index) pairs. 
        # Storing an initial (0, 0) pair will handle edge cases where the 
        # valid subarray starts from index 0
        hash_map = {0: 0}
        
        # Initialize a variable to keep track of the running sum of elements 
        # as we progress through the nums list
        preSum = 0
        
        # Iterate through the list of numbers
        for i in range(len(nums)):
            # Add the current number to the running sum
            preSum += nums[i]
            
            # If the remainder of preSum divided by k is not in the hashmap, 
            # add it along with the current index + 1. The +1 ensures that 
            # the length of any found subarray is at least 2
            if preSum % k not in hash_map:
                hash_map[preSum % k] = i + 1
            
            # If the remainder is in the hashmap and the difference between the 
            # current index and the stored index is at least 1, return True. 
            # This is because we've found a subarray of at least length 2 
            # whose sum is a multiple of k
            elif hash_map[preSum % k] < i:
                return True
        
        # If the loop completes without returning True, no valid subarray was found
        return False

        
# @lc code=end

