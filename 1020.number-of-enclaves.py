#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start

# Related to [200], [1254]
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(m):
            self.dfs(grid, i, 0)
            self.dfs(grid, i, n - 1)

        for j in range(n):
            self.dfs(grid, 0, j)
            self.dfs(grid, m - 1, j)

        num_enclaved = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_enclaved += 1
        
        return num_enclaved
    
    def dfs(self, grid: List[List[int]], i: int, j: int) -> None:

        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0  or i >= m or j >= n or grid[i][j] == 0:
            return 
        
        grid[i][j] = 0

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)



        
# @lc code=end

