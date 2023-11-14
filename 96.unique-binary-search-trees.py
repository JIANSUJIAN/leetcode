#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:

    def __init__(self) -> None:
        # Initialize a memoization table to store results of subproblems
        self.memo = []

    def numTrees(self, n: int) -> int:
        # Create an (n+1) x (n+1) matrix filled with zeros
        self.memo = [[0 for i in range(n+1)] for j in range(n+1)]
        
        # Start the count of unique BSTs possible using numbers from 1 to n
        return self.count(1, n)

    def count(self, lo: int, hi: int) -> int:
        # Base case: An empty tree has one structure
        if lo > hi:
            return 1
        
        # If this subproblem is already solved, return the result from memo
        if self.memo[lo][hi] != 0:
            return self.memo[lo][hi]
        
        # The variable to store the number of unique BSTs from lo to hi
        res = 0

        # Consider each number from 'lo' to 'hi' as a root
        for i in range(lo, hi+1):
            # Calculate the number of left subtrees possible with numbers less than 'i'
            left = self.count(lo, i-1)
            
            # Calculate the number of right subtrees possible with numbers greater than 'i'
            right = self.count(i+1, hi)
            
            # Total number of trees with 'i' as root = (left subtrees * right subtrees)
            res += left * right
        
        # Store the computed result in the memo table before returning
        self.memo[lo][hi] = res
        
        return res

# @lc code=end

