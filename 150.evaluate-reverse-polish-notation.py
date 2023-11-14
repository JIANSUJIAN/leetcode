#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack to hold numbers and intermediate results
        stack = []

        # Iterate through each token in the RPN expression
        for token in tokens:
            # If the token is an operator, pop the necessary operands from the stack,
            # perform the operation, and push the result back onto the stack.
            if token in '+-*/':
                a, b = stack.pop(), stack.pop()  # 'a' and 'b' are operands for the operation
                
                # Perform the corresponding arithmetic operation based on the operator
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(b - a)  # Note: subtraction order matters here
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Division in Python can result in a float, even for integer division.
                    # Using int() ensures we get the floor value of the division.
                    stack.append(int(b / a))  # Note: division order matters here
            else:
                # If the token is not an operator, it's a number. Push it onto the stack.
                stack.append(int(token))

        # At the end of processing all tokens, the final result is on the top of the stack.
        return stack.pop()


        
# @lc code=end

