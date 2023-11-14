#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        # Helper function to perform post-order traversal and return:
        # 1. The maximum depth of leaves in the subtree rooted at 'node'.
        # 2. The lowest common ancestor (LCA) of the deepest leaves in that subtree.
        def helper(node):
            # Base case: If the node is None, it doesn't contribute to depth or LCA.
            if not node:
                return 0, None
            
            # Recursively find the maximum depth and LCA for the left subtree.
            left_depth, left_lca = helper(node.left)
            
            # Recursively find the maximum depth and LCA for the right subtree.
            right_depth, right_lca = helper(node.right)
            
            # Determine the maximum depth and LCA for the subtree rooted at the current node.
            if left_depth > right_depth:
                # The left subtree is deeper. Therefore, the LCA and maximum depth
                # come from the left subtree.
                return left_depth + 1, left_lca
            elif left_depth < right_depth:
                # The right subtree is deeper. Therefore, the LCA and maximum depth
                # come from the right subtree.
                return right_depth + 1, right_lca
            else:
                # Both subtrees have the same depth. This means the deepest leaves
                # are spread across both subtrees, making the current node their LCA.
                # Note: left_depth + 1 and right_depth + 1 would be the same.
                return left_depth + 1, node
        
        # Initiate the post-order traversal from the root node.
        # We're only interested in the LCA of the deepest leaves, so we take the
        # second element of the tuple returned by helper().
        _, lca = helper(root)
        
        # Return the computed LCA.
        return lca

        

        
# @lc code=end

