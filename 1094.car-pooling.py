#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    # The Differnce class is a helper class to manage prefix sums.
    class Differnce:
        # Constructor initializes the difference array.
        def __init__(self, nums: List[int]) -> None:
            self.nums = nums
            self.diff = [0] * (len(nums) + 1)

        # The increment method updates the difference array based on the given range [i, j].
        def increment(self, i: int, j: int, val: int):
            # Increment the start of the range by the given value.
            self.diff[i] += val
            # Decrement the position immediately after the range by the given value.
            self.diff[j + 1] -= val
        
        # The result method computes the prefix sum from the difference array.
        def result(self) -> List[int]:
            res = [0] * len(self.diff)
            res[0] = self.diff[0]
            # Compute the prefix sum.
            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            return res

    # The carPooling method determines if it's possible to complete all trips given the car capacity.
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Initialize an array to represent the number of passengers at each location.
        nums = [0] * 1001
        # Create a Differnce object to manage prefix sums.
        df = self.Differnce(nums)

        # Iterate through each trip in the trips list.
        for trip in trips:
            val = trip[0]  # Number of passengers to pick up.
            i = trip[1]    # Start location.
            j = trip[2] - 1  # End location (adjusted by -1 for correct indexing).
            # Update the difference array based on the trip details.
            df.increment(i, j, val)

        # Compute the prefix sum to get the number of passengers at each location.
        res = df.result()

        # Check if the number of passengers at any location exceeds the car capacity.
        for i in range(len(res)):
            if capacity < res[i]:
                return False
        # If all locations have passengers within capacity, return True.
        return True


        
# @lc code=end

