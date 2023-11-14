#
# @lc app=leetcode id=1644 lang=python3
#
# [1644] Lowest Common Ancestor of a Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) -> None:
        # Flags to check if nodes 'p' and 'q' are found in the tree.
        self.foundP = False
        self.foundQ = False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start the LCA search from the root of the tree.
        res = self.find(root, p.val, q.val)
        
        # If either 'p' or 'q' was not found in the tree, return None.
        if not self.foundP or not self.foundQ:
            return None
        
        return res
    
    def find(self, root, val1, val2):
        # Base case: If we've reached the end of a branch, return None.
        if not root:
            return None
        
        # Recursively search in the left subtree.
        left = self.find(root.left, val1, val2)
        # Recursively search in the right subtree.
        right = self.find(root.right, val1, val2)

        # If both left and right subtrees contain one of the nodes, 
        # the current root is their lowest common ancestor.
        if left and right:
            return root
        
        # If the current root's value matches one of the nodes' values, 
        # update the respective flag to True.
        if root.val == val1 or root.val == val2:
            if root.val == val1:
                self.foundP = True
            if root.val == val2:
                self.foundQ = True
            return root
        
        # Otherwise, if one of the two nodes was found (either in the left or the right subtree),
        # return that node. If neither was found, this will return None.
        return left if left else right


        
# @lc code=end

