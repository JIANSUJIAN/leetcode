#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Initialize the accumulated sum as 0
        self.sum = 0
        # Traverse and modify the tree
        self.traverse(root)
        return root         

    def traverse(self, root: TreeNode) -> None:
        """
        Traverse the tree in a reverse in-order manner (right -> root -> left).
        This ensures that we process nodes with larger values first.
        """
        if not root:
            return
        
        # Traverse the right subtree first (larger values)
        self.traverse(root.right)
        
        # Update the accumulated sum and node's value
        self.sum += root.val
        root.val = self.sum
        
        # Traverse the left subtree
        self.traverse(root.left)

    
# @lc code=end

