#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Initialize an empty string to store the result.
        res = ""
        
        # Iterate through each character of the input string.
        for i in range(len(s)):
            # Check for the longest palindrome centered at `s[i]` (odd length).
            s1 = self.palindrome(s, i, i)
            
            # Check for the longest palindrome centered between `s[i]` and `s[i+1]` (even length).
            s2 = self.palindrome(s, i, i + 1)
            
            # Update `res` with the longest between `res` and `s1`.
            res = res if len(res) > len(s1) else s1
            
            # Update `res` with the longest between `res` and `s2`.
            res = res if len(res) > len(s2) else s2
            
        # Return the longest palindromic substring found.
        return res

    def palindrome(self, s: str, l: int, r: int) -> str:
        # Expand outwards from the center until a non-palindromic boundary is found.
        # Ensure indices don't go out-of-bounds and characters at l and r are equal.
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        # Return the identified palindromic substring.
        # Note: `l` and `r` are incremented and decremented one extra time in the loop, 
        # so we adjust by taking `l+1` and `r`.
        return s[l+1:r]
        
# @lc code=end

