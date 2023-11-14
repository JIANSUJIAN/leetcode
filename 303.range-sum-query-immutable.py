#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize the prefix sum array with an additional 0 at the start.
        # This helps in conveniently calculating the sum for any range.
        self.preSum = [0 for _ in range(len(nums) + 1)]
        
        # Calculate the prefix sum for each position.
        # The prefix sum at position i represents the sum of elements from index 0 to i (inclusive) in nums.
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # To get the sum between any two indices left and right, we subtract:
        # the prefix sum at 'left' from the prefix sum at 'right + 1'
        # This gives the sum of elements from index 'left' to 'right' (both inclusive).
        return self.preSum[right + 1] - self.preSum[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

