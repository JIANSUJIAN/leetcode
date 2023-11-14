#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start

# Approach 1
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        res = []
        temp = [[] for _ in range(m + n - 1)]

        for i in range(m):
            for j in range(n):
                temp[i + j].append(mat[i][j])
        
        for idx, diagnoal in enumerate(temp):
            res += diagnoal if idx % 2 else diagnoal[::-1]
        
        return res


# Approach 2 O(1) Space


        
# @lc code=end

