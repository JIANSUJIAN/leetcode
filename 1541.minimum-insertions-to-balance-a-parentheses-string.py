#
# @lc app=leetcode id=1541 lang=python3
#
# [1541] Minimum Insertions to Balance a Parentheses String
#


# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        # Initialize `res` to track the number of insertions needed to make the string balanced.
        # Initialize `balance` to track how many closing brackets we need to match the existing open brackets.
        res = 0
        balance = 0
        
        for c in s:
            # For every '(' encountered in the string:
            if c == "(":
                # Each opening bracket requires two closing brackets to match.
                # Increase our expected closing brackets by 2.
                balance += 2
                
                # If `balance` is odd, it indicates there's an unmatched ')' before this '('.
                # Increment `res` to account for an additional ')' insertion.
                # Decrement `balance` by 1 to balance out the unmatched ')'.
                if balance % 2 == 1:
                    res += 1
                    balance -= 1
            # For every ')' encountered in the string:
            elif c == ")":
                # We've encountered a closing bracket, so decrement our expected count by 1.
                balance -= 1
                
                # If `balance` becomes -1, it implies there was no '(' to match this ')'.
                # To balance, we need to insert an opening bracket and increase `res`.
                # Additionally, reset `balance` to 1 since we now expect one more closing bracket.
                if balance == -1:
                    res += 1
                    balance = 1
                    
        # At the end of the loop, add `balance` to `res` to get the total number of insertions needed.
        # The `balance` gives the number of unmatched closing brackets, while `res` gives the insertions done so far.
        return res + balance


# @lc code=end
