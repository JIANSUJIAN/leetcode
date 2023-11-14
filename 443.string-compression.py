#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        
        # Iterate over characters in 'chars'
        while i < len(chars):
            # Initialize a variable to track the length of the current group of characters
            group_length = 1
            
            # Loop to check for consecutive same characters
            # and update the group_length accordingly
            while (i + group_length < len(chars) and chars[i + group_length] == chars[i]):
                group_length += 1
            
            # Write the current character to the 'res' position in 'chars'
            chars[res] = chars[i]
            res += 1
            
            # If there's more than one consecutive character,
            # write the group_length after the character in 'chars'
            if group_length > 1:
                str_repr = str(group_length)  # Convert the group length to string
                chars[res:res+len(str_repr)] = list(str_repr)  # Place the count after the character
                res += len(str_repr)  # Move the result pointer by the number of digits in group_length
            
            # Move the 'i' pointer by the group_length to start compressing the next group of characters
            i += group_length
        
        # Return the length of the compressed string
        return res



        
# @lc code=end

