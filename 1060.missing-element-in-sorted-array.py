#
# @lc app=leetcode id=1060 lang=python3
#
# [1060] Missing Element in Sorted Array
#

# @lc code=start

# Approach 1: Iteration
# class Solution:
#     def missingElement(self, nums: List[int], k: int) -> int:

#         n = len(nums)
#         for i in range(1, n):
#             missed_in_gap = nums[i] - nums[i - 1] - 1
#             if missed_in_gap >= k:
#                 return nums[i - 1] + k
#             k -= missed_in_gap

#         return nums[n - 1] + k


# Approach 2: Binary Search
# class Solution:
#     def missingElement(self, nums: List[int], k: int) -> int:
#         # Determine the length of the input array 'nums'.
#         n = len(nums)

#         # Initialize two pointers, 'left' and 'right', to define the search space within the array.
#         left, right = 0, n - 1

#         # Continue the loop until the search space is narrowed down to one element.
#         while left < right:
#             # Calculate the middle index 'mid'. This calculation avoids integer overflow.
#             mid = right - (right - left) // 2
            
#             # Check if the number of missing numbers from nums[0] to nums[mid] is less than 'k'.
#             # (nums[mid] - nums[0]) gives total numbers from nums[0] to nums[mid],
#             # and subtracting 'mid' gives us the number of missing numbers.
#             if (nums[mid] - nums[0]) - mid < k:
#                 # If true, update 'left' to 'mid' since the kth missing number lies to the right of 'mid'.
#                 left = mid
#             else:
#                 # Otherwise, update 'right' to 'mid - 1' since the kth missing number is to the left of 'mid'.
#                 right = mid - 1

#         # Once the loop ends, 'left' points to the last index in the modified search space.
#         # 'nums[0] + k + left' gives the kth missing number.
#         # Explanation 1: nums[0] is a base, 'k' accounts for the missing numbers, and 'left' adjusts based on positions traversed.
#         # elements from the input + missing elements = left + 1 + k
#         # answer - nums[0] + 1 = left + 1 + k -> answer = nums[0] + left + k
#         return nums[0] + k + left 

        

# Labuladong template: 

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Determine the length of 'nums'.
        n = len(nums)

        # Initialize two pointers, 'left' and 'right', to represent the search space.
        left, right = 0, n  # 'right' is set to 'n' to create a [left, right) interval.

        # Perform binary search to find the position where the kth missing element should be.
        while left < right:
            # Compute the middle index of the search space.
            mid = left + (right - left) // 2
            
            # Calculate the number of missing elements within nums[0] to nums[mid].
            # This is done by subtracting the index 'mid' from the difference between 'nums[mid]' and 'nums[0]'.
            missing_elements = (nums[mid] - nums[0]) - mid
            
            # Compare the number of missing elements with 'k'.
            if missing_elements == k:
                # If they are equal, the kth missing number is on the left side of 'mid'.
                right = mid
            elif missing_elements < k:
                # If fewer elements are missing, the kth missing number is on the right side of 'mid'.
                left = mid + 1
            elif missing_elements > k:
                # If more elements are missing, the kth missing number is on the left side of 'mid'.
                right = mid
        
        # Calculate the kth missing number by starting from 'nums[0]' and adding 'k' 
        # and 'left', then subtracting 1 to account for zero-based indexing.
        return nums[0] + k + left - 1

        
        
# @lc code=end

