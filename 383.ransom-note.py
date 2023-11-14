#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        # Initialize a dictionary to store frequency of characters in the magazine.
        char_count = {}
        
        # Populate char_count with characters from the magazine.
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
        # Check if each character of ransomNote can be constructed from the magazine.
        for char in ransomNote:
            # If the character is not in char_count or its count is 0, return False.
            if char not in char_count or char_count[char] == 0:
                return False
            # Decrement the count of the character in char_count.
            char_count[char] -= 1
    
        # If we have processed all characters of ransomNote, return True.
        return True
    
            

        
# @lc code=end

