#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # The prefix_sum dictionary is used to store the frequency of cumulative brick widths.
        # The key intuition here is that if many rows have a brick ending at the same width,
        # drawing a line at that width will cross fewer bricks.
        prefix_sum = {}
        
        # Traverse each row of bricks in the wall.
        for row in wall:
            cumulative_sum = 0
            # Iterate through each brick's width in the current row, but exclude the last brick.
            # We exclude the last brick because the problem specifies that the line cannot be 
            # drawn along one of the two vertical edges of the wall.
            for brick in row[:-1]:
                cumulative_sum += brick  # Cumulatively add the width of bricks.
                
                # Increase the count of the current cumulative sum in the dictionary. 
                # This effectively counts the number of brick "edges" at this position across rows.
                prefix_sum[cumulative_sum] = prefix_sum.get(cumulative_sum, 0) + 1
        
        # The goal is to find where the maximum edges (or gaps) align, as drawing a line there 
        # will lead to crossing the least bricks. If no such gap exists, default to 0.
        max_gaps = max(prefix_sum.values(), default=0)
        
        # The total number of rows minus the maximum gaps gives the number of bricks crossed.
        # This is because for each aligned gap, we avoid one brick.
        return len(wall) - max_gaps

        
# @lc code=end

