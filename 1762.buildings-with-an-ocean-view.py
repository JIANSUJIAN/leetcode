#
# @lc app=leetcode id=1762 lang=python3
#
# [1762] Buildings With an Ocean View
#

# @lc code=start
# Approach 1: Linear Iteration
# From left to right
# Time: O(n) Space: O(n)

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        ans = []
        n = len(heights)

        for current in range(n):
            while ans and heights[ans[-1]] <= heights[current]:
                ans.pop()
            ans.append(current)
        return ans

# Approach 2: Monotonic Stack
# From right to left
# Time: O(n) Spance: O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        n = len(heights)
        ans = []
        stack = []

        for current in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[current]:
                stack.pop()
            
            if not stack:
                ans.append(current)
            
            stack.append(current)
        ans.reverse()
        return ans


# Approach 3: Monotonic Stack (Space Optimization))
# Time: O(n) Space: O(1)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        max_height = -1
        n = len(heights)
        ans = []

        for current in range(n - 1, -1, -1):
            if max_height < heights[current]:
                ans.append(current)
                max_height = heights[current]
        ans.reverse()
        return ans




        
# @lc code=end

