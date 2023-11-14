#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # Initialize the maximum length of LCIS (ans) and the starting index of the current subsequence (anchor) to 0
        ans = anchor = 0
        
        # Iterate through the list of numbers
        for i in range(len(nums)):
            # Check if it's not the first element and the current subsequence has ended
            # (i.e., current number is not greater than the previous one)
            if i and nums[i - 1] >= nums[i]:
                # Set the starting index of the new subsequence to the current index
                anchor = i
                
            # Calculate the length of the current subsequence and update the maximum length (ans) if needed
            ans = max(ans, i - anchor + 1)
            
        # Return the length of the longest continuous increasing subsequence found
        return ans

        
# @lc code=end

