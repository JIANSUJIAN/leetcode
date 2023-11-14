#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start

from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.rand = random.Random()

    def reset(self) -> List[int]:
        return self.nums
        
    def shuffle(self) -> List[int]:
        n = len(self.nums)
        copy = self.nums.copy()

        for i in range(n):
            r = i + self.rand.randint(0, n - i - 1)
            copy[i], copy[r] = copy[r], copy[i]
        return copy

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

