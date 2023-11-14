#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
## 1
# Brute Force
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []  # No solution found

## 2 
# Two-pass Hash Table
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         numMap = {}
#         n = len(nums)

#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i
            
#         # Find the complement
#         for i in range(n):
#             complement = target - nums[i]  
#             if complement in nums and numMap[complement] != i:
#                 return [i, numMap[complement]]
#         return []

## 3
# One-pass Hash Table
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
        
        return []

solution = Solution()

nums = [2, 7, 11, 15]
target = 9


print(solution.twoSum(nums, target))


# @lc code=end
