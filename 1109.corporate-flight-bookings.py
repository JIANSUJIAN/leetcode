#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:

    class Difference:
        def __init__(self, nums: List[int]) -> None:
            assert len(nums) > 0
            self.diff = [0] * len(nums)
            self.diff[0] = nums[0]
            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i-1]

        def increment(self, i: int, j: int, val:int) -> None:
            self.diff[i] += val

            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val
        
        def result(self) -> List[int]:

            res = [0] * len(self.diff)
            res[0] = self.diff[0]

            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            
            return res
            

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        dif = self.Difference(nums)

        for booking in bookings:
            i = booking[0] - 1 
            j = booking[1] - 1
            val = booking[2]
            dif.increment(i, j, val)
        return dif.result()    
        
# @lc code=end

