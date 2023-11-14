#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # `need` stores the count of each character in s1.
        # `window` stores the count of each character in the current sliding window of s2.
        need, window = defaultdict(int), defaultdict(int)

        # Populate the `need` dictionary with characters from s1.
        for c in s1:
            need[c] += 1
        
        # `left` and `right` are the two pointers defining the current window in s2.
        left, right = 0, 0
        # `valid` keeps track of how many characters from `s1` are currently matched in the window of `s2`.
        valid = 0

        # Traverse through s2 using the `right` pointer.
        while right < len(s2):
            c = s2[right]
            right += 1
            
            # If the character is in `need`, update the `window` and check for a match.
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # If the window size is same as size of s1, we check for a valid match and slide the window.
            while right - left >= len(s1):

                # If all characters from s1 are matched in the window, it's a valid inclusion.
                if valid == len(need):
                    return True

                # Slide the window to the right.
                d = s2[left]
                left += 1

                # If the character being removed from the window is in `need`, update the window and valid counters.
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        # If we've gone through the entire s2 without finding a valid inclusion, return False.
        return False


        
# @lc code=end

