#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#


# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # `res` will keep track of the number of characters we need to add
        # to make the string valid.
        # `balance` will monitor the net difference between open and close
        # parentheses at any given point in the string.
        res, balance = 0, 0

        # Iterate over the characters in the string
        for c in s:
            # For every open parenthesis, increase the balance
            if c == "(":
                balance += 1

            # For every close parenthesis, decrease the balance
            if c == ")":
                balance -= 1

            # If balance becomes -1, it means there's an unmatched closing
            # parenthesis. To correct this, we need to add an opening parenthesis
            # before it, which is why we increment `res`.
            # After this correction, we also need to reset the balance for this
            # unmatched closing parenthesis by incrementing it.
            if balance == -1:
                res += 1
                balance += 1

        # The final result is the sum of `res` and any remaining imbalance
        # in the string. This handles the case where there are unmatched opening
        # parentheses at the end.
        return res + balance


# @lc code=end
