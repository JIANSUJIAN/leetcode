#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Flatten the binary tree in place using a modified pre-order traversal.
        """

        # Base Case: If the tree is empty or a leaf node, no further action is required.
        if not root:
            return 
        
        # Recursively flatten the left and right subtrees.
        # This ensures that when we process the root node, its children are already flattened.
        self.flatten(root.left)
        self.flatten(root.right)

        # Post-order processing:

        # Preserve the current left and right subtrees of the root.
        # This is done because we will modify root's left and right pointers,
        # but we still need references to the original subtrees.
        left = root.left
        right = root.right

        # Set the left child of root to None. 
        # This is done because in the final flattened tree, 
        # all nodes should only have right children.
        root.left = None

        # Attach the flattened left subtree to the right of the root.
        # This ensures that the nodes in the left subtree appear before the nodes in the right subtree.
        root.right = left

        # Traverse to the end of the new right subtree (which was originally the left subtree).
        # This is done to find the position where we can attach the original right subtree.
        p = root
        while p.right:
            p = p.right
        
        # Attach the flattened right subtree to the end of the linked list.
        # This ensures that the nodes in the right subtree appear after the nodes in the left subtree.
        p.right = right


        
# @lc code=end

