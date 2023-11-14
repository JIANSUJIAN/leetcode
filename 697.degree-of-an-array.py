#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = {}
        first_occurrence = {}
        last_occurrence = {}

        for idx, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = idx 
            last_occurrence[num] = idx
            counts[num] = counts.get(num, 0) + 1

        ans = len(nums)
        degree = max(counts.values())
        for x in counts:
            if counts[x] == degree:
                ans = min(ans, last_occurrence[x] - first_occurrence[x] + 1)

        return ans 

        
# @lc code=end

