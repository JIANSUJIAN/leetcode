#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))

        rank_dict = {num: rank for rank, num in enumerate(sorted_arr, 1)}

        return [rank_dict[num] for num in arr]
        
# @lc code=end

