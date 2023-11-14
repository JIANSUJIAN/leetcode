#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the last initialized element in both arrays.
        i, j = m - 1, n - 1
        
        # Begin filling nums1 from the end.
        p = len(nums1) - 1 

        # While there are elements left in both arrays, compare and place the larger element at the current position.
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]: 
                nums1[p] = nums1[i]  # If element in nums1 is larger, place it in the current position.
                i -= 1  # Move to the next element in nums1.
            else:
                nums1[p] = nums2[j]  # Else, place the element from nums2 in the current position.
                j -= 1  # Move to the next element in nums2.
            p -= 1  # Move to the next position in nums1.

        # If nums2 still has elements left, fill them into the remaining positions of nums1.
        # This is necessary as nums2 might have smaller elements that haven't been placed in nums1 yet.
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1

        
# @lc code=end

