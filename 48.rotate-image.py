#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the given matrix 90 degrees clockwise in-place.
        """
        # Get the size of the matrix.
        n = len(matrix)

        # Step 1: Transpose the matrix.
        # We swap matrix[i][j] with matrix[j][i] for all i < j.
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row.
        for row in matrix:
            self.reverse(row)

    def reverse(self, arr: List[int]):
        """
        Reverse the given array in-place.
        """
        i, j = 0, len(arr) - 1
        while j > i:
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements at indices i and j.
            i += 1  # Move the left pointer to the right.
            j -= 1  # Move the right pointer to the left.


        
# @lc code=end

