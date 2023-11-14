#
# @lc app=leetcode id=616 lang=python3
#
# [616] Add Bold Tag in String
#

# @lc code=start
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Length of the string
        n = len(s)
        
        # Initialize an array to mark characters that need to be bolded
        bold = [False] * n

        # Iterate through each word in the words list
        for word in words:
            # Find the starting position of the word in the string 's'
            start = s.find(word)
            
            # Loop until all occurrences of the word are found in 's'
            while start != -1:
                # Mark the characters of the word as bold in the bold array
                for i in range(start, start + len(word)):
                    bold[i] = True

                # Find the next occurrence of the word starting from the position just after the current occurrence
                start = s.find(word, start + 1)
        
        # Define the bold tags
        open_tag = "<b>"
        close_tag = "</b>"
        ans = []

        # Iterate through the string 's' to build the result with bold tags
        for i in range(n):
            # If the current character should be bolded and it's either the start of the string 
            # or the previous character was not bolded, append the open tag
            if bold[i] and (i == 0 or not bold[i - 1]):
                ans.append(open_tag)

            # Add the current character to the result
            ans.append(s[i])

            # If the current character should be bolded and it's either the end of the string 
            # or the next character is not bolded, append the close tag
            if bold[i] and (i == n - 1 or not bold[i + 1]):
                ans.append(close_tag)

        # Convert the result list back to a string and return
        return ''.join(ans)



        
# @lc code=end

