#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # `need` stores the count of each character in `p`.
        # `window` stores the count of each character in the current sliding window of `s`.
        need, window = defaultdict(int), defaultdict(int)
        
        # Populate the `need` dictionary with characters from `p`.
        for c in p:
            need[c] += 1

        # `left` and `right` are the two pointers defining the current window in `s`.
        left, right = 0, 0
        # `valid` keeps track of how many characters from `p` are currently matched in the window of `s`.
        valid = 0

        # `res` will store the starting indices of the anagrams.
        res = []

        # Traverse through `s` using the `right` pointer.
        while right < len(s):
            c = s[right]
            right += 1
            
            # If the current character is in `need`, update the `window` and check for a match.
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # If the window size exceeds the size of `p`, slide the window to the right.
            if right - left >= len(p):
                # If all characters from `p` are matched in the window, append the starting index to the result.
                if valid == len(need):
                    res.append(left)

                # Slide the window to the right.
                d = s[left]
                left += 1

                # If the character being removed from the window is in `need`, update the window and valid counters.
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        # Return the list of starting indices.
        return res



        
# @lc code=end

