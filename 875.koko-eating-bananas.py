#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List

class Solution:
    def f(self, piles: List[int], x: int) -> int:
        """Calculate total hours Koko takes to eat all bananas at speed x.
        
        Args:
        - piles: A list of integers representing the number of bananas in each pile.
        - x: The speed at which Koko eats bananas.
        
        Returns:
        - hours: Total number of hours Koko would take to eat all bananas at speed x.
        """
        hours = 0
        for pile in piles:
            # Calculate the hours required to eat 'pile' bananas at speed 'x'
            hours += pile // x

            # If there are any remaining bananas, add an extra hour
            if pile % x > 0:
                hours += 1

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """Determine the minimum speed at which Koko should eat to finish all bananas in h hours.
        
        Args:
        - piles: A list of integers representing the number of bananas in each pile.
        - h: The maximum number of hours Koko has to eat all the bananas.
        
        Returns:
        - Minimum speed Koko should eat at to consume all bananas in h hours.
        """
        # Start with the minimum possible speed
        left = 1
        # Set the initial maximum speed to the maximum pile size
        right = max(piles)
        
        while left < right:
            # Calculate the mid-point of current speed range
            mid = left + (right - left) // 2
            
            # Determine how many hours Koko would take to eat all bananas at speed 'mid'
            total_hours = self.f(piles, mid)
            
            # If it takes exactly 'h' hours at speed 'mid', narrow the search to the left half
            if total_hours == h:
                right = mid
            # If it takes less than 'h' hours at speed 'mid', Koko can potentially eat slower
            elif total_hours < h:
                right = mid
            # If it takes more than 'h' hours, Koko needs to eat faster
            else:
                left = mid + 1
                
        return left

        
# @lc code=end

