#
# @lc app=leetcode id=311 lang=python3
#
# [311] Sparse Matrix Multiplication
#

# @lc code=start

# Approach 1: Naive Iteration

# class Solution:
#     def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
#         ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]

#         for row_index, row_elements in enumerate(mat1):
#             for element_index, row_element in enumerate(row_elements):
#                 if row_element:
#                     for col_index, col_element in enumerate(mat2[element_index]):
#                         ans[row_index][col_index] += row_element * col_element

#         return ans


# Approach 2: List of Lists
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
            rows = len(matrix)
            cols = len(matrix[0])
            compressed_matrix = [[] for _ in range(rows)]

            for row in range(rows):
                for col in range(cols):
                    if matrix[row][col]:
                        compressed_matrix[row].append([matrix[row][col], col])
            return compressed_matrix
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        A = compress_matrix(mat1)
        B = compress_matrix(mat2)

        ans = [[0] * n for _ in range(m)]

        for mat1_row in range(m):
            for element1, mat1_col in A[mat1_row]:
                for element2, mat2_col in B[mat1_col]:
                    ans[mat1_row][mat2_col] += element1 * element2
        return ans



# Approach 3: Yale Format
# class Solution:
#     def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
# @lc code=end

