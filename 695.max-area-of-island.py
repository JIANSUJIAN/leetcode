#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start

# Approach 1: DFS (recursive)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # record max area 
        max_area = 0
 
        def dfs(i: int, j: int) -> int:
            if i <  0 or j < 0 or i >= m or j >= n:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return dfs(i + 1, j) + dfs(i, j + 1) + dfs(i - 1, j) + dfs(i, j - 1) + 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
       
        return max_area


# Approach 2: DFS (iterative)
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
# @lc code=end

