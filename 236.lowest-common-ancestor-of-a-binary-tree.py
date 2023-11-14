#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start the LCA search from the root of the tree with the values of nodes p and q.
        return self.find(root, p.val, q.val)
    
    def find(self, root, val1, val2):
        # If we've reached the end of a branch, return None.
        if not root:
            return None
        
        # If the current root's value matches either of the input values,
        # return the root. This is because if one of the values matches the root,
        # then this node is one of the two nodes we are looking for.
        if root.val == val1 or root.val == val2:
            return root
        
        # Recursively search the left subtree for the nodes.
        left = self.find(root.left, val1, val2)
        # Recursively search the right subtree for the nodes.
        right = self.find(root.right, val1, val2)

        # If the left search found one node and the right search found the other node,
        # then the current root is their LCA.
        if left and right:
            return root
        
        # If only one of the two nodes was found (either in the left or the right subtree),
        # return that node.
        return left if left else right 


        

    
        
# @lc code=end

