#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#

# @lc code=start
class Solution:
    
    class Difference:
        def __init__(self, nums: List[int]) -> None:
            # Ensure the nums list is not empty
            assert len(nums) > 0
            
            # Initialize the difference array with zeros
            self.diff = [0] * len(nums)
            
            # The first element of the difference array is the same as the original array
            self.diff[0] = nums[0]
            
            # Build the difference array where each element is the difference between the current 
            # and the previous element of the original array
            for i in range(1, len(nums)):
                self.diff[i] =  nums[i] - nums[i - 1] 
        
        def increment(self, i: int, j: int, val: int) -> None:
            """Apply the increment operation on the difference array."""
            
            # Increment the start index by the value
            self.diff[i] += val
            
            # Decrement the next index after the end by the value
            # This ensures that the actual increase is only between i and j (inclusive)
            if j + 1 < len(self.diff):
                self.diff[j + 1] -= val
        
        def result(self) -> List[int]:
            """Convert the difference array back to the original array."""
            
            res = [0] * len(self.diff)
            res[0] = self.diff[0]
            
            # Compute the cumulative sum to get the actual values in the original array
            for i in range(1, len(self.diff)):
                res[i] = res[i - 1] + self.diff[i]
            
            return res
            
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Initialize the array with zeros
        nums = [0] * length
        
        # Create the difference array for nums
        dif = self.Difference(nums)
        
        # Apply each update on the difference array
        for update in updates:
            i, j, val = update
            dif.increment(i, j, val)
        
        # Convert the difference array back to the original array and return
        return dif.result()




