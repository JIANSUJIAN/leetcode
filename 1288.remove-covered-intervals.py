#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        Removes covered intervals from the list of intervals.
    
        Args:
        - intervals: List of intervals where each interval is represented as [start, end].
    
        Returns:
        - The count of non-overlapping intervals after removing the covered intervals.
        """
        
        # Sort the intervals based on two criteria:
        # 1. By their starting points in increasing order.
        # 2. If starting points are the same, by their ending points in decreasing order.
        # This ensures that for the same start, larger intervals come first.
        intervals.sort(key=lambda x: (x[0], -x[1]))
    
        # Initialize the left and right pointers using the first interval.
        left, right = intervals[0][0], intervals[0][1]
    
        # Counter for covered intervals.
        res = 0
    
        # Iterate over the sorted intervals, starting from the second one.
        for i in range(1, len(intervals)):
            intv = intervals[i]
            
            # If the current interval is covered by the previous one, increment the counter.
            if left <= intv[0] and right >= intv[1]:
                res += 1
            
            # If there's an overlap with the current interval and its end is outside the previous interval,
            # adjust the right pointer.
            if right >= intv[0] and right <= intv[1]:
                right = intv[1]
            
            # If the current interval starts after the previous interval ends, 
            # update the left and right pointers to the current interval.
            if right < intv[0]:
                left, right = intv[0], intv[1]
    
        # Return the number of intervals minus the count of covered intervals.
        return len(intervals) - res
    # @lc code=end

