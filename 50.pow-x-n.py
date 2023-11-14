#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start

# Approach 1: Recursive
# Time: O(logn) Space: O(logn)
# class Solution:
#     def binaryExp(self, x: float, n: int) -> float:
#         # Base case
#         if n == 0:
#             return 1
        
#         # Handle cases where n < 0
#         if n < 0:
#             return 1.0 / self.binaryExp(x, -1 * n)
        
#         # Perform Binary Exponentiation
#         # If `n` is odd we perform Binary Expoentiation on `n - 1` 
#         # and multiply the result with x
#         if n % 2 == 1:
#             return x * self.binaryExp(x * x, (n - 1) // 2)  ## floor division to return int type
#         else:
#             return self.binaryExp(x * x, n // 2)

#     def myPow(self, x: float, n: int) -> float:
#         return self.binaryExp(x, n)

# Approach 2: Iterative
# Time: O(logn) Space: O(1)
class Solution:
    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        # Handle cases where n < 0
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        # Perform Binary Exponentiation
        result = 1
        while n != 0:
            # If `n` is odd we multiply the result by `x` and reduce `n` by 1
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square `x` and reduce `n` by half, x^n => (x^2)^(n/2)
            x *= x
            n //= 2
        return result

    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)

            
            






        
# @lc code=end

