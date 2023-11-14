#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # Stack to store numbers indicating how many times a substring should be repeated
        countStack = []
        
        # Stack to store substrings that are currently being processed
        resStack = []
        
        # Variable to accumulate digits for multi-digit numbers
        currNum = 0
        
        # Variable to accumulate characters for the current substring being processed
        currStr = ''

        # Iterate over each character in the input string
        for char in s:
            if char.isdigit():
                # Accumulate digits to form the full number (handles multi-digit numbers)
                currNum = currNum * 10 + int(char)
            elif char == '[':
                # Push the current number and substring onto their respective stacks
                # This signifies the start of a new substring that might be repeated
                countStack.append(currNum)
                resStack.append(currStr)
                
                # Reset the number and substring for the next segment inside the brackets
                currNum = 0 
                currStr = ''
            elif char == ']':
                # On encountering a closing bracket:
                # 1. Pop the last stored substring
                # 2. Pop the last stored repetition count
                # 3. Construct the new substring by repeating the current substring
                #    based on the popped repetition count and prepend the popped substring
                prevStr = resStack.pop()
                repeatCount = countStack.pop()
                currStr = prevStr + currStr * repeatCount
            else:
                # If the character is a letter, append it to the current substring
                currStr += char
        
        # Return the fully decoded string
        return currStr

        
# @lc code=end

