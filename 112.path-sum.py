#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 1. Recursion
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
        
#         targetSum -= root.val

#         if not root.left and not root.right:
#             return targetSum == 0
#         return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        
#2. Stack and DFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the tree is empty, no path can be found, return False.
        if not root:
            return False
        
        # Initialize the stack with the root node and the remaining sum 
        # after subtracting the root's value. This will track nodes to visit 
        # and the current running sum for each node.
        stack = [(root, targetSum - root.val)]
        
        # Iterate while there are still nodes to process.
        while stack:
            node, curr_sum = stack.pop()
            
            # Check if the current node is a leaf node (no left or right child) 
            # and the updated sum for this node is zero.
            if not node.left and not node.right and curr_sum == 0:
                return True  # We've found a path from root to leaf with the given sum.
            
            # If the node has a right child, push it onto the stack 
            # with the updated sum after subtracting the child's value.
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            
            # Similarly, if the node has a left child, push it onto the stack 
            # with the updated sum after subtracting the child's value.
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
        
        # If all nodes are processed and no valid path was found, return False.
        return False

# @lc code=end

