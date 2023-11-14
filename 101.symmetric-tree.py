#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the root is None, the tree is symmetric by default.
        if not root:
            return True
        
        # Start by checking if the left subtree is a mirror reflection of the right subtree.
        return self.isSame(root.left, root.right)
    
    def isSame(self, leftroot, rightroot):
        # Base Case: If both the left and right subtrees are None, 
        # it means we've reached the end of both subtrees simultaneously, 
        # hence they are symmetric.
        if leftroot is None and rightroot is None:
            return True
        
        # If only one of the subtrees (either left or right) is None 
        # while the other isn't, then the tree isn't symmetric.
        # This is because one side has more nodes than the other.
        if leftroot is None or rightroot is None:
            return False

        # If the values of the current nodes in the left and right subtrees aren't equal, 
        # the tree isn't symmetric.
        if leftroot.val != rightroot.val:
            return False        

        # Recursive Calls:
        # 1. Compare the right child of the left subtree with the left child of the right subtree.
        # 2. Compare the left child of the left subtree with the right child of the right subtree.
        # Both these recursive checks should return True for the tree to be symmetric.
        return self.isSame(leftroot.right, rightroot.left) and self.isSame(leftroot.left, rightroot.right)

        
# @lc code=end

