#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits for easier manipulation.
        digits = list(str(num))
        
        # Create a dictionary to store the rightmost index of each digit in the number.
        # This helps in finding a larger digit that appears later in the number.
        rightmost = {int(digits[i]): i for i in range(len(digits))}
        
        # Iterate over each digit in the number.
        for i in range(len(digits)):
            # For the current digit, check if there's a larger digit that appears later.
            # We start from 9 (largest possible digit) and go down to the current digit.
            for d in range(9, int(digits[i]), -1):
                # If such a larger digit is found and its rightmost position is to the right 
                # of the current digit's position, we swap them.
                if d in rightmost and i < rightmost[d]:
                    digits[i], digits[rightmost[d]] = digits[rightmost[d]], digits[i]
                    # After swapping, return the number immediately.
                    return int("".join(digits))
        
        # If no swap was performed, the number is already the maximum possible.
        return num


        
# @lc code=end

