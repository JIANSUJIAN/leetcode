#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start

# Approach 1: DFS

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
        
#         m, n = len(grid), len(grid[0])
#         num_islands = 0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     num_islands += 1
#                     self.dfs(grid, i, j)
#         return num_islands
    
#     def dfs(self, grid: List[List[str]], i: int, j: int):
#         m, n = len(grid), len(grid[0])
#         if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
#             return
        
#         grid[i][j] = '0'

#         self.dfs(grid, i + 1, j)
#         self.dfs(grid, i - 1, j)
#         self.dfs(grid, i, j + 1)
#         self.dfs(grid, i, j - 1)
        

# Approach 2: BFS
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Return 0 if the grid is empty.
        if not grid:
            return 0
        
        # Get the dimensions of the grid.
        m, n = len(grid), len(grid[0])
        num_islands = 0

        # Directions for up, down, left, right moves.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Iterate through each cell in the grid.
        for i in range(m):
            for j in range(n):
                # If the cell is land (represented by '1').
                if grid[i][j] == '1':
                    # Increment the island count.
                    num_islands += 1

                    # Initialize the queue with the current cell.
                    # We wrap the tuple (i, j) inside a list to ensure it's added as a single element in the deque.
                    queue = deque([(i, j)])

                    # Mark the cell as visited.
                    grid[i][j] = '0'

                    # BFS traversal.
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in directions:
                            new_x, new_y = x + dx, y + dy
                            # Check if the neighboring cell is within grid boundaries and is land.
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                                # Add the neighboring cell to the queue.
                                # No need to wrap the tuple in a list since append treats its argument as a single element.
                                queue.append((new_x, new_y))
                                
                                # Mark the neighboring cell as visited.
                                grid[new_x][new_y] = '0'

        # Return the total count of islands.
        return num_islands


# Approach 3: Union - Find


                    
    
    



        
# @lc code=end

