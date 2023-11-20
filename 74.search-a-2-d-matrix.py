#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

from typing import List
# @lc code=start


# See https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/wo-xie-le--9c7a4/
# Case 1: basic binarySearch (find a number)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        rows, cols = len(matrix), len(matrix[0])

        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            row = mid // cols
            col = mid % cols
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

        
# @lc code=end

