#
# @lc app=leetcode id=1428 lang=python3
#
# [1428] Leftmost Column with at Least a One
#

# @lc code=start
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# Approach 1: Brute Force
# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         rows, cols = binaryMatrix.dimensions()
#         smallest_index = cols

#         for row in range(rows):
#             for col in range(cols):
#                 if binaryMatrix.get(row, col) == 1:
#                     smallest_index = min(smallest_index, col)
#                     break
#         return -1 if smallest_index == cols else smallest_index


# Approach 2: Binary Search
# Time: O(MlogN) Sapce: O(1)
# class Solution:
#     def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
#         rows, cols = binaryMatrix.dimensions()
#         smallest_index = cols

#         for row in range(rows):
#             lo = 0
#             hi = cols - 1

#             while lo < hi:
#                 mid = (hi + lo) // 2
#                 if binaryMatrix.get(row, mid) == 0:
#                     lo = mid + 1
#                 else:
#                     hi = mid
#             if binaryMatrix.get(row, lo) == 1:
#                 smallest_index = min(smallest_index, lo)
        
#         return -1 if smallest_index == cols else smallest_index

        
# Approach 3: Start at Top Right, Move Only Left and Down

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

# @lc code=end

