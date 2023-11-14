#
# @lc app=leetcode id=356 lang=python3
#
# [356] Line Reflection
#

# @lc code=start
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # Base condition: If there are no points, they are trivially reflected.
        if not points:
            return True
        
        # Convert the list of points into a set for efficient O(1) lookups.
        # We use map to convert each individual list (representing a point) into a tuple,
        # since lists are unhashable and cannot be added to a set. Tuples are hashable.
        point_set = set(map(tuple, points))
        
        # Find the smallest and largest x-coordinates among all points.
        # These will help determine the potential line of reflection.
        min_x = min(point[0] for point in points)
        max_x = max(point[0] for point in points)
        
        # Calculate the potential line of reflection. It's the midpoint between
        # the smallest and largest x-coordinates.
        line_of_reflection = (min_x + max_x) / 2
        
        # For each point in our set, calculate its reflection across the 
        # line_of_reflection and check if this reflected point also exists in our set.
        for x, y in point_set:
            # The reflected point's x-coordinate is calculated as:
            # (2 * line_of_reflection - x). The y-coordinate remains the same.
            if (2 * line_of_reflection - x, y) not in point_set:
                return False  # Reflected point not found, so return False
        
        # If all points' reflections were found in the set, return True.
        return True

# @lc code=end

