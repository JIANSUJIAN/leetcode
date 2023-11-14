#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

##  1
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         # Initialize an empty list to store the result of the preorder traversal.
#         self.res = []

#         # Start the traversal from the root node.
#         self.traverse(root)
        
#         # Return the result list after completing the traversal.
#         return self.res

#     def traverse(self, root: TreeNode) -> None:
#         # Base case: If the current node is None (i.e., we've reached a leaf node or the tree is empty),
#         # we don't need to proceed further.
#         if root is None:
#             return
        
#         # In preorder traversal, we first visit the current node.
#         self.res.append(root.val)
        
#         # After visiting the current node, we recursively traverse its left subtree.
#         self.traverse(root.left)
        
#         # After completing the left subtree, we recursively traverse the right subtree.
#         self.traverse(root.right)

## 2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Initialize an empty list to store the result of the preorder traversal.
        res = []
        
        # Base case: If the tree is empty, return the empty list.
        if not root:
            return res
        
        # In preorder traversal, we first visit the current node.
        res.append(root.val)
        
        # After visiting the current node, we recursively traverse its left subtree.
        # We extend the result list with the result of the recursive traversal of the left subtree.
        res.extend(self.preorderTraversal(root.left))
        
        # After completing the left subtree, we recursively traverse the right subtree.
        # Again, we extend the result list with the result of the recursive traversal of the right subtree.
        res.extend(self.preorderTraversal(root.right))
        
        return res

# @lc code=end

