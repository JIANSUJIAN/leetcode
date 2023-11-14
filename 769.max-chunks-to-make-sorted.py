#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize max_seen to keep track of the highest value seen so far in the array.
        max_seen = -1 
        
        # Initialize count to keep track of the number of chunks.
        count = 0
        
        # Iterate over the array with the index and value.
        for i, num in enumerate(arr):
            # Update max_seen with the highest value encountered so far.
            max_seen = max(max_seen, num)
            
            # If the current index matches max_seen, it means all numbers before 
            # this index (inclusive) are less than or equal to this index, indicating 
            # a possible chunk. Therefore, we increment the count.
            if i == max_seen:
                count += 1
                
        # Return the total number of chunks.
        return count

# @lc code=end

