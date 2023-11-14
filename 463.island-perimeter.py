#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r - 1][c]
                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c - 1]
                    if r == rows - 1:
                        down = 0
                    else:
                        down = grid[r + 1][c]
                    if c == cols - 1:
                        right = 0
                    else:
                        right = grid[r][c + 1]

                    res += 4 - (up+left+right+down)

        return res


        
# @lc code=end

