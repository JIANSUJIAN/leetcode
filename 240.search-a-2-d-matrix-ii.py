#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start

# Approach 1: Binary Search
# Time: O(log(n!)) = O(nlog(n)) # Space: O(1)
# class Solution:
#     def binarySearch(self, matrix: List[List[int]], target: int, start: int, vertical: bool):
#         low = start
#         high = len(matrix[0]) - 1 if vertical else len(matrix) - 1

#         while low <= high:
#             mid = low + (high - low) // 2
#             if vertical:
#                 if matrix[start][mid] < target:
#                     low = mid + 1
#                 elif matrix[start][mid] > target:
#                     high = mid - 1
#                 else:
#                     return True
#             else:
#                 if matrix[mid][start] < target:
#                     low = mid + 1
#                 elif matrix[mid][start] > target:
#                     high = mid - 1 
#                 else:
#                     return True
        
#         return False



#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

#         if not matrix:
#             return False
        
#         # Iterate over the matrix diagonal starting from the top-left
#         for i in range(min(len(matrix), len(matrix[0]))):
#             # Perform binary search in the current row and column
#             vertical_found = self.binarySearch(matrix, target, i, True)
#             horizontal_found = self.binarySearch(matrix, target, i, False)

#             if vertical_found or horizontal_found:
#                 return True

# Approach 2: Divide and Conquer. Recursive
# Time: O(nlogn) Space: O(logn)
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         # Check if the matrix is empty
#         if not matrix:
#             return False

#         # Define a recursive function to search a submatrix
#         def search_recursively(left, up, right, down):
#             # Base case: if submatrix has no area or is invalid
#             if left > right or up > down:
#                 return False
            
#             # Base case: if target is out of the sorted range of the submatrix
#             elif target < matrix[up][left] or target > matrix[down][right]:
#                 return False

#             # Calculate the middle column index
#             mid = left + (right - left) // 2

#             # Search in the middle column for the target
#             row = up
#             while row <= down and matrix[row][mid] <= target:
#                 # If target is found, return True
#                 if matrix[row][mid] == target:
#                     return True
#                 row += 1
            
#             # Recursive case: search in the bottom-left and top-right submatrices
#             # Bottom-left submatrix search (left of mid and below the found row)
#             # Top-right submatrix search (right of mid and above the found row)
#             return search_recursively(left, row, mid - 1, down) or \
#                     search_recursively(mid + 1, up, right, row - 1)
        
#         # Start the recursive search from the full matrix dimensions
#         return search_recursively(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


# Approach 3: Search Sapce Reduction
# Time: O(m + n) Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        height = len(matrix)
        width = len(matrix[0])

        if height == 0 or width == 0:
            return False
        
        # Start out pointers from the bottom-left
        row =  height - 1
        col = 0

        while row >= 0 and col < width:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        
        return False

        

            
        
# @lc code=end

