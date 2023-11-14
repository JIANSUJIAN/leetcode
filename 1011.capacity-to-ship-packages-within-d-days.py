#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List

class Solution:
    def f(self, weights, x) -> int:
        """Calculate the number of days to ship all weights with ship capacity x.
        
        Args:
        - weights: A list of integers representing the weights of items.
        - x: The capacity of the ship.
        
        Returns:
        - days: The total number of days required to ship all weights with ship capacity x.
        """
        days = 0
        i = 0
        while i < len(weights):
            # Remaining capacity of the ship for the current day
            cap = x
            # Fill the ship with weights until its capacity is reached
            while i < len(weights) and cap >= weights[i]:
                cap -= weights[i]
                i += 1
            days += 1
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """Determine the minimum ship capacity to ship all weights within a given number of days.
        
        Args:
        - weights: A list of integers representing the weights of items.
        - days: The maximum number of days to ship all the weights.
        
        Returns:
        - Minimum ship capacity to ship all weights within 'days'.
        """
        # Initialize the left boundary with the maximum weight, since a ship cannot carry less than that.
        left = max(weights)
        
        # Initialize the right boundary with the total sum of weights, a theoretical maximum capacity.
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            # Calculate the number of days required with ship capacity 'mid'
            total_days = self.f(weights, mid)
            
            # If it takes exactly 'days' with capacity 'mid', narrow the search to the left half
            if total_days == days:
                right = mid
            # If it takes fewer days with capacity 'mid', the ship can potentially have a smaller capacity
            elif total_days < days:
                right = mid
            # If it takes more days, the ship needs more capacity
            else:
                left = mid + 1
                
        return left

        
# @lc code=end

