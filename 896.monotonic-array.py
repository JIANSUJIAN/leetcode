#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing =  True

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                decreasing = False
            
            if nums[i] > nums[i+1]:
                increasing = False
        return decreasing or increasing
        
# @lc code=end

