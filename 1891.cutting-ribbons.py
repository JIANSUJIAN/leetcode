#
# @lc app=leetcode id=1891 lang=python3
#
# [1891] Cutting Ribbons
#

# @lc code=start
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # Helper function to calculate the number of ribbons of a given length
        def countRibbons(length):
            # Sum the number of ribbons for each ribbon in the array divided by the given length
            return sum(ribbon // length for ribbon in ribbons)

        # Initialize the lower and upper bounds of the search range
        low, high = 1, max(ribbons)
        # Variable to store the maximum length found so far that meets the requirements
        result = 0

        # Perform binary search within the range [low, high]
        while low <= high:  # Using <= ensures complete exploration of the search space
            # Calculate the midpoint of the current range
            mid = (low + high) // 2
            # Calculate how many ribbons can be made of length 'mid'
            if countRibbons(mid) >= k:
                # If we can make enough ribbons, update result and search for a potentially longer length
                result = mid
                low = mid + 1  # Explore the upper half of the range
            else:
                # If we can't make enough ribbons, try shorter lengths
                high = mid - 1  # Explore the lower half of the range

        return result



# 2. **Approach**: The solution uses a binary search algorithm to efficiently find the maximum ribbon length that meets the requirements.
   
# 3. **Binary Search Algorithm**:
#    - **Search Space**: Defined by `low` (starting at 1, the minimum possible ribbon length) and `high` (initially the length of the longest ribbon in the array).
#    - **Midpoint Evaluation**: In each iteration, the midpoint (`mid`) of the current range is calculated and tested to see how many ribbons of that length can be produced.
#    - **Adjusting the Search Range**: 
#      - If enough ribbons (`>= k`) can be made from `mid`, the search continues in the upper half (`low = mid + 1`) to find if longer ribbons are possible.
#      - If not enough ribbons can be made, the search continues in the lower half (`high = mid - 1`) to try shorter lengths.
#    - **Convergence**: The search narrows down the range until `low` exceeds `high`, ensuring that all possible lengths are considered.

# 4. **countRibbons Function**: A helper function used to calculate the number of ribbons of a given length that can be made from the input array. It sums up the quotient of each ribbon length divided by the current test length (`mid`).

# 5. **Ensuring Complete Search**: The condition `low <= high` in the binary search loop ensures that the algorithm fully explores the search space, including the endpoints, and doesn't miss any possible solution, especially when `low` equals `high`.

# 6. **Result**: The function returns the maximum length of the ribbons that can be cut to meet the requirement of `k` ribbons, or `0` if it's not possible to obtain `k` ribbons of the same length.


        
# @lc code=end

