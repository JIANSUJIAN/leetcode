#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path into individual components (directories or special symbols)
        tokens = path.split('/')

        # Stack to store valid directory names as we process the tokens
        stack = []

        for token in tokens:
            # If we encounter '..', it means move up one directory.
            # So, we pop from the stack unless it's already empty.
            if token == '..':
                if stack:
                    stack.pop()
            # If the token is not empty and not '.', it's a valid directory name.
            # Push it onto the stack.
            elif token and token != '.':
                stack.append(token)
        
        # Construct the canonical path by joining the directory names in the stack
        # with a forward slash as a separator, and ensure the path starts with a slash.
        return '/' + '/'.join(stack)

        
# @lc code=end

