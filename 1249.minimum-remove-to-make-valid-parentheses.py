#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start

# # Approach 1: Using a Stack and String Builder
# # Time O(n) Space: O(n)
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         # This set will hold indices of all unmatched parentheses that need to be removed.
#         indexes_to_remove = set()
        
#         # This stack will help match opening parentheses '(' with their corresponding closing ones ')'.
#         stack = []

#         # First pass: Identify unmatched parentheses.
#         for i, c in enumerate(s):
#             # Ignore characters that are not parentheses.
#             if c not in "()":
#                 continue
            
#             # If it's an opening parenthesis, add its index to the stack.
#             if c == "(":
#                 stack.append(i)
#             elif not stack:
#                 # If there's a closing parenthesis without a matching opening one, mark its index for removal.
#                 indexes_to_remove.add(i)
#             else:
#                 # If there's an opening parenthesis available in the stack, pop it off (it's matched).
#                 stack.pop()

#         # Any remaining indices in the stack represent unmatched opening parentheses. 
#         # Add these indices to our removal set.
#         indexes_to_remove = indexes_to_remove.union(set(stack))

#         # Second pass: Construct the result string by skipping characters at indices in our removal set.
#         string_Builder = []
#         for i, c in enumerate(s):
#             if i not in indexes_to_remove:
#                 string_Builder.append(c)
        
#         # Convert the list of characters back to a string and return.
#         return "".join(string_Builder)



# Approach 2: Two Pass String Builder
# see also [2116]
# Time O(n) Space: O(n)

# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
        
#         def delete_invalid_closing(string, open_symbol, close_symbol):
#             sb = []  # StringBuilder to build the resulting string
#             balance = 0  # To track the balance of the parentheses
            
#             for c in string:
#                 # Increase the balance for each open symbol
#                 if c == open_symbol:
#                     balance += 1
#                 # Decrease the balance for each close symbol and skip it if unmatched
#                 if c == close_symbol:
#                     if balance == 0:
#                         continue
#                     balance -= 1
#                 sb.append(c)  # Add the character to the resulting string
#             return "".join(sb)

#         # First, remove all unmatched closing parentheses
#         s = delete_invalid_closing(s, "(", ")")
        
#         # Reverse the string and then remove all unmatched opening parentheses
#         s = delete_invalid_closing(s[::-1], ")", "(")
        
#         # Return the correctly formatted string
#         return s[::-1]

# Approach 3:  Shortened Two Pass String Builder
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        # First pass: remove all invalid ')'
        first_pass_chars = []
        open_seen_count = 0 
        balance = 0

        for c in s:
            if c == '(':
                balance += 1
                open_seen_count += 1
            
            if c == ')':
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(c)
        
        # Second pass: Remove the rightmost '('
        result = []
        open_to_keep_count = open_seen_count - balance
        for c in first_pass_chars:
            if c == '(':
                open_to_keep_count -= 1
                if open_to_keep_count < 0:
                    continue
            result.append(c)

        return ''.join(result)

        
        
    
            

        
# @lc code=end

