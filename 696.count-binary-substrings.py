#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start

# # Approach 1: Groups by character
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         # Traverse the binary string and count consecutive 0s and 1s
#         counts = []
#         count = 1
#         for i in range(1, len(s)):
#             if s[i] == s[i - 1]:
#                 count += 1
#             else:
#                 counts.append(count)
#                 count = 1
#         counts.append(count) # Append the last count

#         # Iterate through the list and sum up the minimum of each pair.
#         res = 0
#         for i in range(1, len(counts)):
#             res += min(counts[i], counts[i - 1])
#         return res


# Approach 2: Linear Scan
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize answer to 0. 
        # prev stores the length of the previous streak, and cur is for the current streak.
        ans = 0
        prev = 0 
        cur = 1

        # Iterate over the string from the second character
        for i in range(1, len(s)):
            # If current character is different from the previous, a streak has ended.
            if s[i - 1] != s[i]:
                ans += min(prev, cur)  # Count the number of valid substrings for this streak.
                prev, cur = cur, 1 # Reset streak counters.
            else:
                cur += 1 # If same character as previous, continue the streak.
            
        # Count the valid substrings from the final streak.
        ans += min(prev, cur)
        return ans





        
# @lc code=end

