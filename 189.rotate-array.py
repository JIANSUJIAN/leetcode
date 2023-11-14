#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start

# 1 reverse method O(1) space 

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n

#         nums.reverse()

#         nums[:k] = reversed(nums[:k])
#         nums[k:] =reversed(nums[k:])

# class Solution:

#     def reverse_arr(self, arr, i, j):

#         while (i < j):
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#         return arr

#     def rotate(self, nums: List[int], k: int) -> None:

#         if k > len(nums):
#             k %= len(nums)
        
#         if k > 0:
#             self.reverse_arr(nums, 0, len(nums) - 1)
#             self.reverse_arr(nums, 0, k - 1)
#             self.reverse_arr(nums, k, len(nums) - 1)

   
  
# 2 using extra arry
# O(n) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n ] = nums[i]
        nums[:] = rotated


        
# @lc code=end

