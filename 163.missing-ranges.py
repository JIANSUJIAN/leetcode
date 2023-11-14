#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        missing_ranges = []
        n = len(nums)

        if n == 0:
            missing_ranges.append([lower, upper])
            return missing_ranges

        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i] + 1, nums[i + 1] - 1])
        
        if upper > nums[n - 1]:
            missing_ranges.append([nums[n - 1] + 1, upper])
        
        return missing_ranges


        
# @lc code=end

