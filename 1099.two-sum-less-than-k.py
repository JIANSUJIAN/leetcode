#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#

# @lc code=start
# two pointers
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()
        ans = -1
        left, right = 0, len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum < k:
                ans = max(ans, sum)
                left += 1
            else:
                right -= 1
        return ans


        
# @lc code=end

