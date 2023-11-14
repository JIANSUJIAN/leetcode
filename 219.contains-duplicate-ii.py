#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        idx_dict = {}

        for i, num in enumerate(nums):
            if num in idx_dict and abs(i - idx_dict[num]) <= k:
                return True
            idx_dict[num] = i
        return False
        
# @lc code=end

