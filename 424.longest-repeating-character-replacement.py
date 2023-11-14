#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Initialize left pointer and character frequency dictionary
        l = 0
        c_frequency = {}

        # Variable to store the length of the longest substring with all same characters after replacements
        longest_str_len = 0

        # Iterate over the string using right pointer.
        for r in range(len(s)):
            # Update the frequency count of the currect character
            c_frequency[s[r]] = c_frequency.get(s[r], 0) + 1

            # Calculate the length of the current window.
            window_len = r - l + 1

            # Calculate the number of replacements required to make all characters in the current window the same.
            # This is determined by total characters in the window units minus the frequency of the most common character.
            replacements_required = window_len - max(c_frequency.values())

            # If the replacements required is within the limit, update the answer
            if replacements_required <= k:
                longest_str_len = max(longest_str_len, r - l + 1)
            else:
                # If replacements required exceed the limit, slide the window by moving the left pointer.
                c_frequency[s[l]] -= 1
                # If a chacater's frequency becomes 0, we can remove it from the dictionary. 
                if c_frequency[s[l]] == 0:
                    del c_frequency[s[l]]
                l += 1
        return longest_str_len
            

# @lc code=end

