#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Base case: If n is 0, return an empty list
        if n == 0:
            return []
        
        # Start building the trees using numbers from 1 to n
        return self.build(1, n)
    
    def build(self, lo: int, hi: int) -> List[TreeNode]:
        # Initialize a list to store the root nodes of the unique BSTs
        res = []

        # Base case: If low exceeds high, append a None (indicating end of tree) and return
        if lo > hi:
            res.append(None)
            return res
        
        # Consider each number from 'lo' to 'hi' as a potential root
        for i in range(lo, hi+1):
            
            # Recursively generate all possible left subtrees using numbers less than 'i'
            leftTree = self.build(lo, i-1)
            
            # Recursively generate all possible right subtrees using numbers greater than 'i'
            rightTree = self.build(i+1, hi)

            # Iterate through each combination of left and right subtrees
            for left in leftTree:
                for right in rightTree:
                    
                    # Create a new root node with value 'i'
                    root = TreeNode(i)
                    
                    # Attach the left and right subtrees to the root
                    root.left = left
                    root.right = right 
                    
                    # Append the new tree to the result list
                    res.append(root)
                    
        # Return the list of unique BSTs
        return res


        
# @lc code=end

