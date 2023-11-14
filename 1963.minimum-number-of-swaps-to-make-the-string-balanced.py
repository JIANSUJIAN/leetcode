#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        # Initialize a balance variable to keep track of the imbalance in the string.
        # If it's positive, it represents the unmatched '[' characters.
        # If it's negative, it represents the unmatched ']' characters.
        balance = 0

        # Traverse the string character by character
        for c in s:
            if c == '[':
                # Increment the balance for every '['
                balance += 1
            else:
                # Only decrement the balance if there's a preceding unmatched '['
                # This ensures we're only counting unmatched brackets, 
                # as a matching ']' decreases the balance.
                if balance > 0:
                    balance -= 1

        # The formula `(balance + 1) // 2` calculates the minimum number of swaps
        # needed to balance the string. We only need to correct half of the imbalances,
        # because each swap corrects two positions.
        return (balance + 1) // 2

        
# @lc code=end

