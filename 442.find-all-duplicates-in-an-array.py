#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
## 1 
## Hash set
## Sapce: O(n) Time: O(n)
# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         res = []
#         n = len(nums)

#         seen = [0] * (n + 1)
#         for num in nums:
#             if seen[num] == 0:
#                 seen[num] = 1
#             else:
#                 res.append(num)

#         return res
        
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # List to store the numbers that appear twice
        res = []

        # Iterate through the numbers in the list
        for num in nums:
            # Convert the number to its corresponding index (1-based to 0-based)
            index = abs(num) - 1
            
            # If the number at the derived index is negative, 
            # this means the current number has been seen before, thus it's a duplicate.
            if nums[index] < 0:
                res.append(abs(num))
            else:
                # Otherwise, negate the number at the derived index to mark it as seen.
                nums[index] *= -1
        
        # Return the list of numbers that appear twice
        return res

        
        
# @lc code=end

