#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## 1
## Traverse
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Start the process of tree inversion.
        self.traverse(root)
        return root
    
    def traverse(self, root: TreeNode):
        # Base case: If the node is None, return immediately.
        if not root:
            return 
        
        # Swap the left and right subtrees.
        # We don't need to swap the values of the nodes. Instead, we swap the subtrees themselves.
        # root.left, root.right = root.right, root.left
        temp = root.val
        root.left = root.right
        root.right = temp

        # Recursively invert the left subtree.
        self.traverse(root.left)
        # Recursively invert the right subtree.
        self.traverse(root.right)

## 2
## Divide
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Base case: if the node is None (i.e., leaf node or empty tree), return None.
        if root is None:
            return None
        
        # Recursively invert the left subtree. After this call, the left subtree rooted at `root.left` is inverted.
        left = self.invertTree(root.left)
        # Recursively invert the right subtree. After this call, the right subtree rooted at `root.right` is inverted.
        right = self.invertTree(root.right)

        # Swap the inverted left and right subtrees. 
        root.left = right
        root.right = left

        # Return the current root so it can be used by the recursive calls in the higher layers.
        return root

        

# @lc code=end

