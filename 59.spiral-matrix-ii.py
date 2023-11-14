#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        upper_bound, lower_bound = 0, n - 1
        left_bound, right_bound = 0, n - 1

        num = 1
        
        while num <= n * n:
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound+1):
                    matrix[upper_bound][j] = num
                    num += 1
                upper_bound += 1
            
            if left_bound <= right_bound:
                for i in range(upper_bound, lower_bound+1):
                    matrix[i][right_bound] = num
                    num += 1
                right_bound -= 1
            
            if upper_bound <= lower_bound:
                for j in range(right_bound, left_bound-1, -1):
                    matrix[lower_bound][j] = num
                    num += 1
                lower_bound -= 1
            
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound-1, -1):
                    matrix[i][left_bound] = num
                    num += 1
                left_bound += 1
        return matrix


            


        
# @lc code=end

