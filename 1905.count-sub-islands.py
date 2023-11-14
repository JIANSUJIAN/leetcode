#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # Retrieve dimensions of the grid
        m, n = len(grid2), len(grid2[0])

        # For each land cell in grid2 that doesn't exist in grid1, mark it as water
        # This is done to remove parts of islands in grid2 that aren't overlapped by grid1
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    self.dfs(grid2, i ,j)
        
        count = 0
        # Count the remaining islands in grid2, which are sub-islands
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    count += 1
                    # Mark the entire island in grid2 to avoid recounting
                    self.dfs(grid2, i ,j)
        return count

    def dfs(self, grid: List[List[int]], i: int, j: int) -> None:
        # Retrieve dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Base cases: Out of bounds or cell is water
        if i < 0 or j < 0 or i >= m or j >= n:
            return 
        if grid[i][j] == 0:
            return
        
        # Mark the current cell as visited (water)
        grid[i][j] = 0 
        
        # Recursively explore all neighboring cells
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)




        
# @lc code=end

