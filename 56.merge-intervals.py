#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge all overlapping intervals and return an array of the non-overlapping intervals.
        
        Args:
        - intervals: A list of pairs, where each pair represents a start and end of an interval.
        
        Returns:
        - A list of merged intervals.
        """

        # If the input list is empty, return an empty list.
        if not intervals:
            return []
        
        # Sort the intervals based on their start values.
        intervals.sort(key=lambda x: x[0])

        # Initialize the result list with the first interval.
        res = [intervals[0]]

        # Iterate over the rest of the intervals.
        for interval in intervals[1:]:
            # Get the last interval in the result list.
            last = res[-1]

            # If the start of the current interval is less than or equal to the end of the last interval in the result,
            # then there is an overlap. Update the end of the last interval in the result if needed.
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            # If there's no overlap, simply add the current interval to the result list.
            else:
                res.append(interval)
        
        # Return the merged intervals.
        return res

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

# @lc code=end

