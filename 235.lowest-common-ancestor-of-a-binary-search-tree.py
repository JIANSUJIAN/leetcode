#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
        # Determine the smaller and larger values between p and q.
        # This ensures we always proceed in the direction where both nodes can be found.
        val1 = min(p.val, q.val)
        val2 = max(p.val, q.val)
        
        # Initiate the search for the lowest common ancestor.
        return self.find(root, val1, val2)

    def find(self, root, val1, val2) -> TreeNode:
        # Base case: if the current node is None, return None.
        if not root:
            return None
        
        # If current node's value is greater than the larger value,
        # it means both nodes are in the left subtree.
        if root.val > val2:
            return self.find(root.left, val1, val2)
        # If current node's value is less than the smaller value,
        # it means both nodes are in the right subtree.
        elif root.val < val1:
            return self.find(root.right, val1, val2)
        else:
            # If the current node's value is between val1 and val2 (inclusive),
            # then this node is the lowest common ancestor of both nodes.
            return root
        
# @lc code=end

