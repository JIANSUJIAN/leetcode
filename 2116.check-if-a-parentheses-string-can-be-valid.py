#
# @lc app=leetcode id=2116 lang=python3
#
# [2116] Check if a Parentheses String Can Be Valid
#

# @lc code=start
class Solution(object):
    def canBeValid(self, s, locked):
        # Odd-length strings can't be valid since every '(' needs a matching ')'
        if len(s) % 2:  
            return False

        # First traversal (left to right)
        # Treat all unlocked characters as '('. If at any point we have more ')' than '(',
        # it means there's a ')' that can't be matched by any previous '('.
        balance = 0
        for i in range(len(s)):
            # If the current character is '(' or it's unlocked, increment the balance
            # Otherwise (if it's a locked ')'), decrement the balance
            balance += 1 if s[i] == '(' or locked[i] == '0' else -1
            
            # If balance goes negative, there are unmatched ')' that can't be balanced
            if balance < 0:
                return False

        # Second traversal (right to left)
        # Treat all unlocked characters as ')'. If at any point we have more '(' than ')',
        # it means there's a '(' that can't be matched by any previous ')'.
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            # If the current character is ')' or it's unlocked, increment the balance
            # Otherwise (if it's a locked '('), decrement the balance
            balance += 1 if s[i] == ')' or locked[i] == '0' else -1
            
            # If balance goes negative, there are unmatched '(' that can't be balanced
            if balance < 0:
                return False

        # If we've gone through both traversals without imbalance, the string can be balanced
        return True

        
# @lc code=end

