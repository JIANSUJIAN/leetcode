#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#

# @lc code=start
class Solution:
    def minAreaRect(self, points):

        min_area = float('inf')
        seen = set(map(tuple, points))

        for i, p1 in enumerate(points):
            x1, y1 = p1
            for j, p2 in enumerate(points):
                x2, y2 = p2
                if i != j and x1 != x2 and y1 != y2 and (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(y2 - y1) * abs(x2 - x1)
                    min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0



# @lc code=end

