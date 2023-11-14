#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
## 1 
## Set 
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         maxLength = 0 # The maxLength variable keeps track of the length of longest substring encountered so far
#         # We use a set (charSet) to keep track of unique characters in the current substring
#         charSet = set()
#         # We maintain two pointers, left and right, to represent the boundries of the current window
#         left = 0

#         for right in range(n): # Iterate through the string using the right pointer
#             if s[right] not in charSet: # If the current character is not in the set, it means we have a new unique character
#                 charSet.add(s[right]) # Then we insert the character into the set
#                 maxLength = max(maxLength, right - left + 1) # And update the maxLength if necessary
#             else: # If the current character is already in the set, it indicates a repeating character within the current substring
#                 while s[right] in charSet: 
#                     # In this case, we move left pointer forward, removing characters from the set until
#                     # the repeating character is no longer present
#                     charSet.remove(s[left])
#                     left += 1
#                 charSet.add(s[right]) # We insert the current character into the set and continue the iteration
#         return maxLength # Finally, we return the maxLength as the length of the longest substring without repeating characters


## 2 
## Dictionary
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we use a dictionary to store the character as the key, 
        # the last index where the character has been seen as value.
        charMap = {} 
        n = len(s)
        maxLength = 0
        left = 0

        for right in range(n): # Iterate the string using right pointer
            if s[right] not in charMap or charMap[s[right]] < left: # If the current character is not in the map,
                                                                    # or its index is less than left then it is a new unique character
                charMap[s[right]] = right # Then we update the charMap with the character's index
                maxLength = max(maxLength, right - left + 1) # and update the maxLength if necessary
            else: # If the character is repeating within the current substring (i.e. in the map), 
                left = charMap[s[right]] + 1 #  then we move the left pointer to the next position after the last occurrence index of the character 
                charMap[s[right]] = right # we update the index of the current character in the charMap and continue the iteration

        return maxLength # at the end, we return the maxLength as the longest substring without repeating characters

## 3
## sliding windows
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # `window` dictionary keeps track of the characters in the current window and their counts.
#         window = {}
        
#         # `left` and `right` are the two pointers defining the current window in `s`.
#         left, right = 0, 0
        
#         # `res` keeps track of the maximum length of substring without repeating characters.
#         res = 0

#         # Traverse through the string using the `right` pointer.
#         while right < len(s):
#             c = s[right]  # Current character
#             right += 1  # Move the right pointer to the right
#             # Increment the count of the current character in the window.
#             window[c] = window.get(c, 0) + 1

#             # If there are duplicates of the current character in the window, slide the window to the right.
#             while window[c] > 1:
#                 d = s[left]  # Character to be removed from the window
#                 left += 1  # Move the left pointer to the right
#                 window[d] -= 1  # Decrement the count of the removed character

#             # Update the result with the maximum length of the current window.
#             res = max(res, right - left)

#         return res




# solution = Solution()
# s = "tmmzuxt"
# print(solution.lengthOfLongestSubstring(s))

        
# @lc code=end

