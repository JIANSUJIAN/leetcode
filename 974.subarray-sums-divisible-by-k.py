#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Initialize count of subarrays and prefix sum modulo
        count, prefix_modulo = 0, 0
        
        # Dictionary to store the frequency of each prefix modulo.
        # Initialized with {0: 1} because we have a prefix sum of 0 by default.
        modulo_freq = {0: 1}

        # Iterate through each number in the list.
        for num in nums:
            # Update the prefix modulo
            prefix_modulo = (prefix_modulo + num) % k
            
            # Python's % can produce negative result, adjust to make it non-negative
            prefix_modulo = (prefix_modulo + k) % k
            
            # Increment count by the number of subarrays ending at the current number 
            # that have a sum divisible by k.
            count += modulo_freq.get(prefix_modulo, 0)
            
            # Update the frequency of the current prefix modulo. 
            modulo_freq[prefix_modulo] = modulo_freq.get(prefix_modulo, 0) + 1
        
        # Return the total count of subarrays with sum divisible by k.
        return count 

        
# @lc code=end

