#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start

from typing import List
from collections import deque

# Approach 1:  Breadth-first Search (Without Overwriting the Input)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m - 1][n - 1] == 1:
            return -1
        
        q = deque()
        visited = [[False for _ in range(m)] for _ in range(n)]

        q.append([0, 0])
        visited[0][0] = True
        pathLen = 1

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        while q:
            size = len(q)
            for _ in range(size):
                current = q.popleft()
                x, y = current[0], current[1]
                if x == m - 1 and y == n - 1:
                    return pathLen
                for i in range(8):
                    nextX = x + dirs[i][0]
                    nextY = y + dirs[i][1]
                    if 0 <= nextX < m and 0 <= nextY < n and not visited[nextX][nextY] and grid[nextX][nextY] == 0:
                        q.append([nextX, nextY])
                        visited[nextX][nextY] = True
            pathLen += 1
        return -1


        







    
    
        
# @lc code=end

