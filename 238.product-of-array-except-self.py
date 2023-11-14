#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element at index i is the product of all 
        elements in the original array except the one at index i.
        
        Args:
        - nums: List of integers.
        
        Returns:
        List of integers representing the product of the array except for the current index.
        """
        
        # Length of the input array.
        n = len(nums)
        
        # Initialize the result array with 1s. Each element will be updated with 
        # the product of all elements except the one at its index.
        result = [1] * n 
        
        # Prefix and postfix products, initialized to 1.
        prefix_product, postfix_product = 1, 1 

        # Update result array with both prefix and postfix products in a single loop.
        # For each 'i', the loop computes the prefix product for the 'i'th element and 
        # the postfix product for the 'n-i-1'th element.
        for i in range(n): 
            result[i] *= prefix_product 
            prefix_product *= nums[i]

            result[n - i - 1] *= postfix_product 
            postfix_product *= nums[n - i - 1]

        return result


        
# @lc code=end

