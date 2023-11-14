#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, preorder, idx, lower=float('-inf'), upper=float('inf')):
        """
        Recursive function to construct the binary search tree from its preorder traversal.
        
        Parameters:
        - preorder: List of integers representing the preorder traversal.
        - idx: List with a single integer representing the current index in the preorder list.
        - lower: The lower bound for the current node's value.
        - upper: The upper bound for the current node's value.
        
        Returns:
        - The constructed TreeNode.
        """
        
        # Base case: Stop if all elements of preorder are used.
        if idx[0] == len(preorder):
            return None
        
        val = preorder[idx[0]]

        # If the current value is not within the valid BST range, return None.
        if val < lower or val > upper:
            return None
        
        # Update the index to process the next value in preorder.
        idx[0] += 1
        root = TreeNode(val)

        # Construct the left subtree, ensuring values are less than the current root value.
        root.left = self.helper(preorder, idx, lower, val)
        # Construct the right subtree, ensuring values are greater than the current root value.
        root.right = self.helper(preorder, idx, val, upper)

        # Return the constructed node.
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        Initiates the recursive construction of the BST from its preorder traversal.
        
        Parameters:
        - preorder: List of integers representing the preorder traversal.
        
        Returns:
        - The root of the constructed BST.
        """
        idx = [0]  # Initialize index.
        return self.helper(preorder, idx)

        
# @lc code=end

