#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize dictionaries to count characters in `t` and in the current window of `s`.
        need, window = defaultdict(int), defaultdict(int)
        
        # Count characters needed from string `t`.
        for c in t:
            need[c] += 1

        # Initialize two pointers `left` and `right` to represent the current window.
        left, right = 0, 0
        # `valid` keeps track of how many characters from `t` are currently satisfied in the window.
        valid = 0
        
        # Variables to keep track of the smallest valid window found.
        start, length = 0, float('inf')

        # Expand the window using the `right` pointer.
        while right < len(s):
            c = s[right]
            right += 1

            # If the character is needed, update the `window` dictionary and check if it satisfies a character from `t`.
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # Try to reduce the window size using the `left` pointer while ensuring the window remains valid.
            while valid == len(need):
                # Update the smallest window if the current one is smaller.
                if right - left < length:
                    start = left
                    length = right - left
                
                # Move the left pointer to the right to try and reduce the window size.
                d = s[left]
                left += 1
                # If the character is needed, update the `window` dictionary and check if the window is still valid.
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        # Return the smallest valid window, or an empty string if no valid window was found.
        return "" if length == float('inf') else s[start:start + length]

                




# @lc code=end

