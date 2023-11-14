#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start

# Approach 1: Sort
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]


# Approach 2: Divide and Conquer
        
# @lc code=end

