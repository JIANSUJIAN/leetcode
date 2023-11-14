#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

## 1. Horizontal scanning
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
        
#         prefix = strs[0]

#         for string in strs:
#             i = 0 
#             while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
#                 i += 1
            
#             prefix = prefix[:i]

#             if not prefix:
#                 return ""
        
#         return prefix

## 2. Vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Return empty string if input list is empty
        if not strs:
            return ""
        
        # Loop through each character of the first string (reference string)
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            # Check if this character is the same at position 'i' for all strings
            for string in strs[1:]:
                # If we have reached the end of the current string or the characters don't match
                if i == len(string) or string[i] != char:
                    # Return the prefix until position 'i' of the reference string
                    return strs[0][:i]
        
        # If loop completes, the whole first string is the common prefix
        return strs[0]




        
# @lc code=end

