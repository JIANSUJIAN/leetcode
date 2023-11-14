#
# @lc app=leetcode id=870 lang=python3
#
# [870] Advantage Shuffle
#

# @lc code=start
import heapq

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Get the length of the input list nums1
        n = len(nums1)

        # Create a max-heap (by negating values of nums2) to efficiently track 
        # the largest value in nums2 along with its index
        maxpq = [(-val, i) for i, val in enumerate(nums2)]
        heapq.heapify(maxpq)
        
        # Sort nums1 in ascending order to easily pick values 
        # from either end based on the current largest value in nums2
        nums1.sort()

        # Pointers to track the leftmost and rightmost unchecked values in nums1
        left, right = 0, n - 1
        
        # Initialize the result list with zeros
        res = [0] * n

        # Process all values in nums2
        while maxpq:
            # Extract the current largest value from nums2 and its index
            val, i = heapq.heappop(maxpq)
            
            # Convert the negated value back to its original form
            maxval = -val
            
            # If the largest value in nums2 is smaller than the largest value in nums1, 
            # then assign the largest value from nums1 to the result
            if maxval < nums1[right]:
                res[i] = nums1[right]
                right -= 1
            # Otherwise, assign the smallest value from nums1 to the result
            else:
                res[i] = nums1[left]
                left += 1

        # Return the reorganized nums1 list as per the advantage condition
        return res

        
# @lc code=end

