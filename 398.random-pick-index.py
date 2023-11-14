#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start

import random


# Approach 1: Reservoir Sampling
# class Solution:

#     def __init__(self, nums: List[int]):
#         self.rand = random.Random()
#         self.nums = nums

#     def pick(self, target: int) -> int:
#         count = 0
#         res = -1
#         n = len(self.nums)

#         for i in range(n):
#             if self.nums[i] != target:
#                 continue
#             count += 1
#             if self.rand.randint(1, count) == 1:
#                 res = i
#         return res

# Approach 2: Caching results using a hashmap
class Solution:
    def __init__(self, nums: List[int]):
        # Dictionary to store the indices for each number in nums
        self.index_map = {}

        # Iterate through the list of numbers and populate the index_map
        for idx, num in enumerate(nums):
            # If the number is already a key in index_map, append the current index
            if num in self.index_map:
                self.index_map[num].append(idx)
            # Otherwise, create a new entry in index_map for this number
            else:
                self.index_map[num] = [idx]

    def pick(self, target: int) -> int:
        # Use random.choice to randomly select one of the indices 
        # for the target number from index_map and return it
        return random.choice(self.index_map[target])



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

