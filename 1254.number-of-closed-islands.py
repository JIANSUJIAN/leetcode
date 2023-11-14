#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#

# @lc code=start

# Related to [200]
# Approach 1: DFS
class Solution:
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for j in range(n):
            self.dfs(grid, 0, j)
            self.dfs(grid, m - 1, j)
        
        for i in range(m):
            self.dfs(grid, i, 0)
            self.dfs(grid, i, n - 1)

        closed_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    closed_islands += 1
                    self.dfs(grid, i, j)
        return closed_islands
       
    def dfs(self, grid: List[List[int]], i: int, j: int):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 1:
            return
        
        grid[i][j] = 1

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1 )
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)


# Approach 2: DFS

        
# @lc code=end

