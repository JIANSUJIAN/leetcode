#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Edge case: If k is 1 or less, no subarray product can be strictly less than k.
        if k <= 1:
            return 0
        
        # Initialize two pointers and a variable to hold the product of the elements.
        left = 0  # left pointer which moves rightwards
        product = 1  # to hold the product of elements in the current subarray
        count = 0  # to count subarrays satisfying the condition
        
        # Iterate through the array with the right pointer
        for right, val in enumerate(nums):
            product *= val  # Update the product with the new element added to the window
            
            # While the product is not less than k, update the product by dividing 
            # it by the leftmost element and move the left pointer rightwards.
            while product >= k:
                product /= nums[left]
                left += 1
            
            # Update the count. The window (left to right) gives a subarray 
            # satisfying the condition. Any subarray ending at 'right' and starting 
            # from left to right will also satisfy. So, add all such subarrays.
            # (right - left + 1) gives the number of such subarrays.
            count += right - left + 1
        
        return count

            


# @lc code=end

