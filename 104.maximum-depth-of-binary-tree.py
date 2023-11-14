#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Initialize the result (maximum depth found so far) and 
        # current depth (used during traversal) as instance variables.
        # Set both to zero initially.
        self.res = 0
        self.depth = 0
        
        # Start the depth-first traversal from the root.
        self.traverse(root)
        
        # Once the traversal is complete, return the maximum depth found.
        return self.res

    def traverse(self, root: TreeNode) -> None:
        # Base Case: If the current node is None (i.e., we've reached a leaf node or the tree is empty),
        # we don't need to proceed further.
        if not root:
            return 
        
        # As we go deeper into the tree, we increment our current depth.
        self.depth += 1 
        
        # If the current node is a leaf node (i.e., it doesn't have left or right children),
        # we compare the current depth with the maximum depth found so far and update it if necessary.
        if not root.left and not root.right:
            self.res = max(self.res, self.depth)
        
        # Recursive Step:
        # We then proceed to traverse the left subtree of the current node.
        self.traverse(root.left)
        # After the left subtree is explored, we do the same for the right subtree.
        self.traverse(root.right)
        
        # As we backtrack (i.e., finish exploring both children of a node and move up),
        # we decrement our current depth.
        self.depth -= 1

        
# @lc code=end

