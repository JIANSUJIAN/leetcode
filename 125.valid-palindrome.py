#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a list to store alphanumeric characters from the input string 's'.
        als = []
    
        # Iterate through the string 's'.
        # Add each alphanumeric character to the list 'als' after converting to lowercase.
        # This ensures our palindrome check is case-insensitive.
        for c in s:
            if c.isalnum():
                als.append(c.lower())
    
        # Convert the list of alphanumeric characters back to a string.
        s = "".join(als)
    
        # Initialize two pointers at the start and end of the cleaned string.
        left, right = 0, len(s) - 1
    
        # Check if the characters at the current pointer positions are the same.
        # Move the pointers towards each other until they meet.
        while left < right:
            if s[left] != s[right]:
                return False  # Characters are different, so it's not a palindrome.
            left += 1
            right -= 1
    
        # If the loop completes without returning False, the string is a palindrome.
        return True
        
# @lc code=end

