#
# @lc app=leetcode id=1676 lang=python3
#
# [1676] Lowest Common Ancestor of a Binary Tree IV
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Convert the list of nodes to a set of values for O(1) lookup time.
        values = set(node.val for node in nodes)
        
        # Start the LCA search from the root of the tree with the set of node values.
        return self.find(root, values)
    
    def find(self, root, values):
        # Base case: If we've reached the end of a branch, return None.
        if not root:
            return None
        
        # If the current root's value is in our set of values,
        # it means this node is one of the nodes we are looking for.
        if root.val in values:
            return root
        
        # Recursively search in the left subtree.
        left = self.find(root.left, values)
        # Recursively search in the right subtree.
        right = self.find(root.right, values)

        # If both left and right subtrees contain nodes from our list,
        # the current root is their lowest common ancestor.
        if left and right:
            return root
        
        # Otherwise, if one of the two nodes was found (either in the left or the right subtree),
        # return that node. If neither was found, this will return None.
        return left if left else right

        
# @lc code=end

