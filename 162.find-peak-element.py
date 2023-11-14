#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start

# Approach 1: Linear Scan
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:

#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 return i
#         return len(nums) - 1


#  Approach 2: Recursive Binary Search
# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         return self.search(nums, 0, len(nums) - 1)

#     def search(self, nums: List[int], l: int, r: int) -> int:
        
#         if l == r:
#             return l
        
#         mid = l + (r - l) // 2

#         if nums[mid] > nums[mid + 1]:
#             return self.search(nums, l, mid)
#         return self.search(nums, mid + 1, r)
        

#  Approach 3: Iterative Binary Search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l



        
        
# @lc code=end

