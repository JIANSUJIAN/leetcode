#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
import random
# Approach 1: Prefix Sums with Linear Search

# class Solution:

#     def __init__(self, w: List[int]):
#         self.prefix_sums = []
#         prefix_sum = 0

#         for weight in w:
#             prefix_sum += weight
#             self.prefix_sums.append(prefix_sum)

#         self.total_sum = prefix_sum

#     def pickIndex(self) -> int:

#         target = self.total_sum * random.random()

#         for i, prefix_sum in enumerate(self.prefix_sums):
#             if target < prefix_sum:
#                 return i

# Approach 2: Prefix Sums with Binary Search

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        # binary search (left bound)
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

