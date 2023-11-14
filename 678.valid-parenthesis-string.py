#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start

# # Approach 1: two pass greedy 
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize two counters:
        # min_count: minimum number of unmatched open parentheses (most pessimistic count).
        # max_count: maximum number of unmatched open parentheses (most optimistic count).
        min_count, max_count = 0, 0
        
        # Traverse through the string to manage the ambiguity introduced by '*'
        for char in s:
            # If the character is '(', increment both counters
            if char == '(':
                min_count += 1
                max_count += 1
            # If the character is ')', decrement both counters
            elif char == ')':
                min_count -= 1
                max_count -= 1
            else:  # char is '*'
                min_count -= 1  # Worst case: treat '*' as ')'
                max_count += 1  # Best case: treat '*' as '('
            
            # If max_count becomes negative at any point, it means we have too many unmatched ')'
            # Thus, the string cannot be valid
            if max_count < 0:
                return False
            
            # If min_count goes negative, it means we might have unmatched ')'
            # To counteract this, assume some '*' were '(' to balance out. Reset min_count to 0.
            if min_count < 0:
                min_count = 0
        
        # After traversing the entire string, if min_count is 0, it means every '(' has found a match.
        # Thus, the string can be valid. Return True. Otherwise, return False.
        return min_count == 0


#  Approach 2: Stack
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         lefts, stars = [], []

#         for idx, char in enumerate(s):
#             if char == '(':
#                 lefts.append(idx)
#             elif char == '*':
#                 stars.append(idx)
#             else:
#                 if lefts:
#                     lefts.pop()
#                 elif stars:
#                     stars.pop()
#                 else:
#                     return False
        
#         # After travering, check if every '(' has a matching '*' that comes after
#         while lefts and stars:
#             if lefts[-1] < stars[-1]:
#                 lefts.pop()
#                 stars.pop()
#             else:
#                 return False
        
#         return not lefts


# Approach 3: 



        
# @lc code=end

