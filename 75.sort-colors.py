#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort the list nums in-place containing three distinct elements: 0, 1, and 2.
        This is a variant of the Dutch National Flag problem.
        """
        # `p0` is the position where the next 0 should be placed.
        # `p2` is the position where the next 2 should be placed.
        p0 = curr = 0
        p2 = len(nums) - 1

        # Iterate through the list while the current pointer `curr` is less than or equal to `p2`.
        while curr <= p2:
            # If the current element is 0, swap it with the element at `p0`
            # and move the `p0` and `curr` pointers to the right.
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            # If the current element is 2, swap it with the element at `p2`
            # and move the `p2` pointer to the left.
            # Notice we don't move the `curr` pointer here because the swapped element
            # could be 0, which should be further processed.
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
            # If the current element is 1, just move the `curr` pointer to the right.
            else:
               curr += 1 

# @lc code=end

