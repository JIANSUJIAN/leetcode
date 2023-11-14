#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start

## 1 
## Two pointers, sliding window
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Get the lengths of both the haystack and the needle.
        m = len(haystack)
        n = len(needle)
        
        # We will try to slide the 'needle' over the 'haystack'
        # The maximum starting position for needle in haystack is 'm - n' (inclusive).
        # Therefore, we loop until 'm - n + 1' (exclusive)
        for window_start in range(m - n + 1):
            
            # For each starting position, we try to match characters
            # between the haystack and needle.
            for i in range(n):
                
                # If any character does not match, we break and try the next position
                if needle[i] != haystack[window_start + i]:
                    break
                
                # If we reach the end of the needle (i == n - 1) 
                # and all characters have matched, we found our position.
                if i == n - 1:
                    return window_start
        
        # If we've exhausted all positions and did not find a match, return -1.
        return -1


        
# @lc code=end

