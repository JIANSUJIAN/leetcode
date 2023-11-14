#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        # Initialize the variable 'area' to store the maximum area found
        area = 0

        # Continue unitl the two pointers meet
        while left < right: 
            # Calculate the area
            cur_area = min(height[left], height[right]) * (right - left)
            area = max(cur_area, area)

            # To potentially find a larger area, we need to move the pointer 
            # pointing to the shorter line. This is because moving the taller line inwards 
            # won't help in achieving a larger area. The width is decreasing, 
            # so to compensate, we aim for a larger height.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
        
# @lc code=end

