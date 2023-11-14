#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 1 
# class Solution:
#     def __init__(self) -> None:
#         # Initialize the maximum diameter to 0.
#         self.maxDiameter = 0

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         # Start the traversal from the root node.
#         self.traverse(root)
#         # Return the computed maximum diameter.
#         return self.maxDiameter

#     def traverse(self, root: TreeNode) -> None:
#         if not root:
#             return 

#         # Calculate the maximum depth of the left and right subtrees.
#         leftMax = self.maxDepth(root.left)
#         rightMax= self.maxDepth(root.right)

#         # The diameter at the current node is the sum of the depths of the left and right subtrees.
#         myDiameter = leftMax + rightMax

#         # Update the global maximum diameter if the current diameter is greater.
#         self.maxDiameter = max(self.maxDiameter, myDiameter)

#         # Continue the traversal for left and right children.
#         self.traverse(root.left)
#         self.traverse(root.right)

#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0

#         # Calculate the maximum depth of the left and right subtrees.
#         leftMax = self.maxDepth(root.left)
#         rightMax = self.maxDepth(root.right)

#         # The depth at the current node is 1 + maximum depth of its left or right subtree.
#         return 1 + max(leftMax, rightMax)


## 2
class Solution:
    def __init__(self) -> None:
        # Initialize the maximum diameter to 0.
        # This variable will store the result.
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # The primary function that will be called to compute the diameter.
        # It begins by finding the maximum depth and in the process, updates the diameter.
        self.maxDepth(root)
        # Return the computed diameter.
        return self.maxDiameter
    
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the node is None, its depth is 0.
        if root is None:
            return 0

        # Recursively find the maximum depth of the left subtree.
        leftMax = self.maxDepth(root.left)
        # Recursively find the maximum depth of the right subtree.
        rightMax = self.maxDepth(root.right)

        # The diameter at the current node (or the number of nodes on the longest path through this node)
        # is the sum of the maximum depths of its left and right subtrees.
        myDiameter = leftMax + rightMax

        # Update the global maximum diameter with the maximum of the current diameter and the previous maximum.
        self.maxDiameter = max(self.maxDiameter, myDiameter)

        # The depth of a node is 1 plus the maximum of the depths of its left and right children.
        return 1 + max(leftMax, rightMax)

# The improved code calculates the diameter in a bottom-up manner. 
# Starting from the leaf nodes, it computes the depth of each node and, in the process, 
# calculates the diameter using the depths of the left and right subtrees. 
# This ensures that each node is visited only once, making the code efficient.

    






        
# @lc code=end

